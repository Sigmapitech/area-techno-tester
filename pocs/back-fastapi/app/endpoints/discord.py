import httpx
import uuid
from fastapi import (
    APIRouter,
    Depends,
    Query,
    HTTPException,
    Header,
)
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from ..config import settings
from ..db import get_session
from .auth import get_user_from_token

router = APIRouter()

DISCORD_SCOPE = "identify guilds"
token_store = {}


@router.get("/connect")
async def discord_connect(token: str = Query(...)):
    # discord forbids any query params, so we have to store our jwt another way.
    state = str(uuid.uuid4())
    token_store[state] = token

    url = (
        f"{settings.discord_api_base}/oauth2/authorize"
        f"?client_id={settings.discord_client_id}"
        f"&redirect_uri={settings.discord_redirect_uri}"
        f"&response_type=code"
        f"&scope={DISCORD_SCOPE}"
        f"&state={state}"
    )

    return RedirectResponse(url)


@router.get("/auth")
async def discord_auth(
    code: str,
    state: str = Query(...),
    db: AsyncSession = Depends(get_session),
):
    jwt_token = token_store.pop(state, None)

    if jwt_token is None:
        raise HTTPException(status_code=401, detail="No token provided")

    user = await get_user_from_token(db, f"Bearer {jwt_token}")

    async with httpx.AsyncClient() as client:
        data = {
            "client_id": settings.discord_client_id,
            "client_secret": settings.discord_client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": settings.discord_redirect_uri,
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        resp = await client.post(
            f"{settings.discord_api_base}/oauth2/token",
            data=data,
            headers=headers,
        )

    if resp.status_code != 200:
        raise HTTPException(
            status_code=resp.status_code, detail="Failed to authenticate with Discord"
        )

    tokens = resp.json()
    print(user.id, tokens)

    user.discord_access_token = tokens["access_token"]
    user.discord_refresh_token = tokens["refresh_token"]
    user.discord_expires_in = tokens["expires_in"]

    db.add(user)
    await db.commit()
    await db.refresh(user)

    # TODO: is there a better way?
    return HTMLResponse(
        content=f"""
        <script>
          window.opener.postMessage(
            {{
              type: 'DISCORD_CONNECTED',
              payload: {{ userId: {user.id} }}
            }},
            window.origin
          );
          window.close();
        </script>
        <p>Discord linked successfully. You can close this window.</p>
    """
    )


@router.get("/list_guilds")
async def discord_list_guilds(
    db: AsyncSession = Depends(get_session),
    authorization: str | None = Header(None),
):
    user = await get_user_from_token(db, authorization or "")

    print(user.id, user.discord_access_token, user.discord_refresh_token)

    if not user.discord_access_token:
        raise HTTPException(status_code=401, detail="Discord not connected")

    async with httpx.AsyncClient() as client:
        print("==>", user)
        token = getattr(user, "discord_access_token")
        print("==>", token)

        headers = {"Authorization": f"Bearer {user.discord_access_token}"}
        print(headers)
        resp = await client.get(
            f"{settings.discord_api_base}/users/@me/guilds", headers=headers
        )

    print(resp)
    if resp.status_code != 200:
        raise HTTPException(
            status_code=resp.status_code, detail="Failed to fetch guilds"
        )

    return resp.json()
