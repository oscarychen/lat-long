import re
import math
from itertools import chain
from typing import Tuple, Union
from .types import Direction


class LatLongParser:
    '''
    Parses string input of coordinates in various formats into lat and long parts.
    '''

    def __init__(self):
        self.expressions = (
            ("^(-*\d+.\d*), *(-*\d+.\d*)$", self._parse_exp_1),
            ("^(\d+)°{0,1}(\d*)'*(\d*).{0,1}(\d*)\"*([S,N]) *(\d+)°{0,1}(\d*)'*(\d*).{0,1}(\d*)\"*([W,E])$", self._parse_exp_2),
        )

    def parse(self, value: str) -> Union[Tuple[int, int, float, Direction, int, int, float, Direction], None]:
        for exp, func in self.expressions:

            match = re.match(exp, value)
            if match:
                return func(match)

    def _parse_exp_1(self, match):
        lat, long = match.groups()
        return self._convert_lat_long_decimal_to_dms(float(lat), float(long))

    def _parse_exp_2(self, match) -> Tuple[int, int, float, Direction, int, int, float, Direction]:
        '''
        Parse function for matching DMS syntax, returns a tuple of DMS parts. ie:
        51°04'20.8"N114°08'03.3"W -> (51, 4, 20.8, 'N', 114, 8, 3.3, 'W')
        '''
        lat_degree_str, lat_minute_str, lat_second_str, lat_second_decimal, s_n, \
            long_degree_str, long_minute_str, long_second_str, long_second_decimal, e_w = match.groups()

        return tuple(chain(
            self._convert_dms_string_parts_to_dms(lat_degree_str, lat_minute_str, lat_second_str, lat_second_decimal),
            s_n,
            self._convert_dms_string_parts_to_dms(long_degree_str, long_minute_str,
                                                  long_second_str, long_second_decimal),
            e_w))

    def _convert_dms_string_parts_to_dms(self, degree_str: str, minute_str: str, second_str: str, second_decimal_str: str) -> Tuple[int, int, float]:
        '''
        Converts a DMS latitude OR longitude syntax, returns a tuple of DMS parts. ie:
        51°04'20.8"N114°08'03.3 -> (51, 4, 20.8)
        '''
        lat_degree = int(degree_str)
        lat_minute = int(minute_str) if minute_str else 0
        lat_second = float(f"{second_str}.{second_decimal_str}") if second_decimal_str else 0
        return lat_degree, lat_minute, lat_second

    def _convert_lat_long_decimal_to_dms(self, lat: float, long: float):
        '''
        Converts decimal coordinates to DMS, returns a tuple of DMS parts. ie:
        -51.07243737494296,-179.13425063752352 -> (51, 4, 20.77454979464676, 'S', 179, 8, 3.302295084627076, 'W')
        '''
        lat_degree, lat_minute, lat_second = self._convert_decimal_to_dms(lat)
        long_degree, long_minute, long_second = self._convert_decimal_to_dms(long)
        s_n = Direction.SOUTH if lat < 0 else Direction.NORTH
        e_w = Direction.WEST if long < 0 else Direction.EAST
        return lat_degree, lat_minute, lat_second, s_n, long_degree, long_minute, long_second, e_w

    def _convert_decimal_to_dms(self, val: float):
        '''
        Converts decimal coordinate syntax to DMS, returns a tuple of DMS parts. +/- ignored. ie:
        -51.07243737494296 -> 51, 4, 20.77454979464676
        '''

        if val > 0:
            degree = math.floor(val)
        else:
            degree = math.ceil(val)

        remainder = (val - degree) * 60
        if remainder > 0:
            minute = math.floor(remainder)
        else:
            minute = math.ceil(remainder)
        remainder -= minute
        second = remainder * 60
        return abs(degree), abs(minute), abs(second)
