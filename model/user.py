# coding: UTF-8
# Date: 2022/1/20
# Author: Leon

from pydantic import BaseModel
from typing import Optional
from config import DEFAULT_AVATAR


class LoginModel(BaseModel):
    username: str
    password: str


class RegisterModel(LoginModel):
    email: str
    avatar: Optional[str] = DEFAULT_AVATAR


class UserModel(RegisterModel):
    id: int
    is_admin: bool
    alive: bool


