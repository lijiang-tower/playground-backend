# coding: UTF-8
# Date: 2022/1/31
# Author: Leon


from pydantic import BaseModel, validator
from typing import Dict, Optional


class CityInfo(BaseModel):
    name: str
    localtime: str
    lat: float
    lon: float


class AirQuality(BaseModel):
    co: float
    no2: float
    o3: float
    so2: float
    pm2_5: float
    pm10: float


class CurrentWeather(BaseModel):
    temp_c: float
    humidity: float
    is_day: bool
    wind_dir: str
    wind_mph: float
    wind_kph: float
    pressure_mb: float
    feelslike_c: float
    air_quality: Optional[AirQuality]


class ApiData(BaseModel):
    location: CityInfo
    current: CurrentWeather
