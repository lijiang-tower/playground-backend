# coding: UTF-8
# Date: 2022/1/20
# Author: Leon

from sanic import Sanic
from sanic.response import json
from os import getenv
from sanic_jwt import initialize
from tortoise.contrib.sanic import register_tortoise

from util.find_blueprints import autodiscover
from util.user_auth import authenticate
import view

app = Sanic('playground-backend')
app.update_config('./config.py')
autodiscover(
    app,
    view,
    recursive=True,
    url_prefix='/api'
)

register_tortoise(
    app,
    db_url=getenv('SANIC_DB_URL'),
    modules={
        "models": ["orm.user", "orm.schedule"]
    },
    generate_schemas=False
)

initialize(app, authenticate=authenticate, secret="j933f234f#$f34jF@f44G.54g,/hc092")


@app.get("/")
async def root(request):
    return json({"msg": "Hello world!"}, 200)


if __name__ == '__main__':
    app.run(
        host=app.config.INTERFACE,
        port=app.config.PORT,
        auto_reload=app.config.AUTO_RELOAD,
        workers=app.config.WORKERS,
        debug=app.config.DEBUG,
        reload_dir='.'
    )
