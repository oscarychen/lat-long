from typing import Union
from .types import Direction
from .parser import LatLongParser


class Coordinates():

    def __init__(self) -> None:
        self.lat_degree: int = 0
        self.lat_minute: int = 0
        self.lat_second: float = 0
        self.s_n = Direction.SOUTH
        self.long_degree: int = 0
        self.long_minute: int = 0
        self.long_second: float = 0
        self.e_w = Direction.EAST

    def from_str(self, coor_str, raise_exception=True):
        parser = LatLongParser()
        parts = parser.parse(coor_str)
        if parts:
            # TODO: some validations should be done here
            self.lat_degree, self.lat_minute, self.lat_second, self.s_n,\
                self.long_degree, self.long_minute, self.long_second, self.e_w = parts
        elif raise_exception is True:
            raise Exception(f"Failed to parse string to coordinates: {coor_str}")

    def from_dms(self, lat_degree: int, lat_minute: int, lat_second: Union[int, float], south_north: Direction,
                 long_degree: int, long_minute: int, long_second: Union[int, float], east_west: Direction):
        # TODO: some validations should be done here
        self.lat_degree = lat_degree
        self.lat_minute = lat_minute
        self.lat_second = lat_second
        self.s_n = south_north
        self.long_degree = long_degree
        self.long_minute = long_minute
        self.long_second = long_second
        self.e_w = east_west

    def __str__(self) -> str:
        return f"{self.lat_degree}°{self.lat_minute}'{self.lat_second}\"{self.s_n} {self.long_degree}°{self.long_minute}'{self.long_second}\"{self.e_w}"
