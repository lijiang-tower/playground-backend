# coding: UTF-8
# Date: 2022/1/20
# Author: Leon

from sanic import Blueprint
from sanic.response import json
from sanic_jwt.decorators import protected
from orm.schedule import Schedule
import os


bp_schedule = Blueprint('schedule', url_prefix=f"/{os.path.abspath(__file__).split('/')[-2]}")


@bp_schedule.get("/list")
@protected()
async def schedule_list(request):
    schedule = await Schedule.filter().values()
    return json(schedule)


@bp_schedule.post("/new_schedule")
@protected()
async def new_schedule(request):
    if request.json is None:
        return json({})
    schedule_data = request.json.get("data") or None
    if schedule_data:
        return json(schedule_data)
    return json({})
