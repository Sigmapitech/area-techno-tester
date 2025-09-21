from pydantic import BaseModel


class Message(BaseModel):
    message: str


class AuthResponse(BaseModel):
    token: str
