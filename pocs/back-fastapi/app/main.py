import logging
import os
import sys
from contextlib import asynccontextmanager
from http import HTTPStatus

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import FileResponse, JSONResponse

from . import endpoints
from .config import settings
from .db import init_db

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)

if "dev" in sys.argv:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=("http://localhost" "http://127.0.0.1:*"),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

endpoints.register_all(app)


@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request, exc: StarletteHTTPException):
    if exc.status_code == HTTPStatus.NOT_FOUND.value:
        if request.url.path.startswith("/api/"):
            return JSONResponse(
                status_code=HTTPStatus.NOT_FOUND.value,
                content={"detail": "API endpoint not found"},
            )

    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


def main():
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
