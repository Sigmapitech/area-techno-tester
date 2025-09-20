from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI(redoc_url="/doc", docs_url=None)


class Message(BaseModel):
    message: str


@app.get(
    "/",
    response_model=Message,
    description="API root to test API response",
    responses={
        200: {
            "content": {
                "application/json": {
                    "example": Message(message="Hello, World!").model_dump()
                }
            },
        }
    },
)
async def example_json():
    return JSONResponse({ "message": "Hello, World!" })


@app.post(
    "/echo",
    response_model=Message,
    description="Echoes back the message sent in the request body",
    responses={
        200: {
            "content": {
                "application/json": {
                    "example": Message(message="Your message here").model_dump()
                }
            }
        }
    },
)
async def echo_message(msg: Message):
    return JSONResponse({"message": msg.message})
