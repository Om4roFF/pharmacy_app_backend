from typing import Optional

from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class Login(BaseModel):
    email: EmailStr
    password: Optional[str] = None
    idToken: Optional[str] = None
