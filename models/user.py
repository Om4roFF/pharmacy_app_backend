import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, validator, constr


class User(BaseModel):
    id: Optional[int] = None
    email: str
    hashed_password: str
    photo_url: str
    google_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserIn(BaseModel):
    email: EmailStr
    google_id: str
    password: str
    matching_password: str
    photo_url: str
    token_id = str

    @validator("matching_password")
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError("password don't match")
        return v
