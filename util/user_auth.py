# coding: UTF-8
# Date: 2022/1/20
# Author: Leon

from sanic_jwt import exceptions
from orm.user import User
import hashlib


async def authenticate(request, *args, **kwargs):
    if request.json is None:
        raise exceptions.AuthenticationFailed("Missing username or password.")
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    user = await User.get_or_none(username=username)
    if user is None:
        raise exceptions.AuthenticationFailed("User not found.")

    if hashlib.sha256(bytes(password, encoding='utf-8')).hexdigest() != user.password:
        raise exceptions.AuthenticationFailed("Password is incorrect.")
    return user
