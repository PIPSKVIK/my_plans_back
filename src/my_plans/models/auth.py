from pydantic import BaseModel
from typing import Optional


class BaseUser(BaseModel):
    email: str
    username: str
    address: Optional[str]
    phone: Optional[str]
    status: Optional[str]
    nickname: Optional[str]
    bio: Optional[str]
    is_active: Optional[bool] = False
    is_admin: Optional[bool] = False


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True  # Если мы его булем из orm доставать, у него будет orm_mode


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
