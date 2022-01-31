# coding: UTF-8
# Date: 2022/1/31
# Author: Leon

from os import getenv
from sanic import Blueprint
from sanic.response import json
from util.weather_handler import get_current_data
from model.weather import WeatherRequest

bp_weather = Blueprint('weather', url_prefix='/weather')


@bp_weather.get('/')
async def weather_api_get(request):
    result = await get_current_data(
        token=getenv('WEATHER_API_TOKEN'),
        city='Shanghai',
        aqi=False
    )
    return json(result.dict())


@bp_weather.post('/')
async def weather_api_post(request):
    r_data = WeatherRequest(**request.json)
    if r_data.type == 'current':
        result = await get_current_data(
            token=getenv('WEATHER_API_TOKEN'),
            city=r_data.city,
            aqi=r_data.aqi
        )
        return json(
            result.dict()
        )
    return json({})
