from datetime import datetime
from meteostat import Daily, Point
from pandas.core.frame import DataFrame


def get_temperature_series(latitude: float, longitude: float, altitude: int, start: datetime, end: datetime) -> DataFrame:
    if start > end:
        start, end = end, start

    point = Point(latitude, longitude, altitude)
    data: DataFrame = Daily(point, start, end).fetch()
    return data["tavg"]
