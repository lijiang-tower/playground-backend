# coding: UTF-8
# Date: 2022/1/20
# Author: Leon

from sanic import Blueprint
from sanic.response import json
from sanic_jwt.decorators import protected
from sanic_pydantic import webargs
from orm.user import User
from model.user import UserModel, LoginModel, RegisterModel
import os


bp_user = Blueprint('user', url_prefix=f"/{os.path.abspath(__file__).split('/')[-2]}")


@bp_user.post('/login')
@webargs(body=LoginModel)
async def user_login(request, **kwargs: LoginModel):
    return json(kwargs.get('payload'))


@bp_user.post('/register')
@webargs(body=RegisterModel)
async def user_register(request, **kwargs: RegisterModel):
    return json(kwargs.get('payload'))
