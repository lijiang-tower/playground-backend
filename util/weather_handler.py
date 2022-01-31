# coding: UTF-8
# Date: 2022/1/31
# Author: Leon

import requests_async as requests
from model.weather import ApiData


async def get_current_data(token: str, city: str, aqi: bool = False) -> ApiData:
    url = f"https://api.weatherapi.com/v1/current.json?key={token}&q={city}&aqi={'yes' if aqi else 'no'}"
    print(url)
    r = await requests.get(
        url
    )
    print(dict(r.json()))
    data = ApiData(**r.json())
    return data

