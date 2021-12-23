from typing import Union, Tuple, overload
from .types import Direction
from .parser import LatLongStringParser


class Coordinates:

    precision = 7

    @overload
    def __init__(self, lat=None, long=None) -> None:
        ...

    @overload
    def __init__(self, lat_degree=None, lat_minute=None, lat_second=None, s_n=None,
                 long_degree=None, long_minute=None, long_second=None, e_w=None) -> None:
        ...

    @overload
    def __init__(self, *args, **kwargs) -> None:
        ...

    def __init__(self, *args, **kwargs) -> None:
        expected_decimal_kwargs = ("lat", "long")
        expected_dms_kwargs = ("lat_degree", "lat_minute", "lat_second", "s_n",
                               "long_degree", "long_minute", "long_second", "e_w")

        self.lat = None
        self.long = None
        self.lat_degree = None
        self.lat_minute = None
        self.lat_second = None
        self.s_n = None
        self.long_degree = None
        self.long_minute = None
        self.long_second = None
        self.e_w = None

        if self._init_kwarg_validator(expected_decimal_kwargs, **kwargs) is True:
            self.from_decimals(**kwargs)
        elif self._init_kwarg_validator(expected_dms_kwargs, **kwargs) is True:
            self.from_dms(**kwargs)
        elif self._init_args_validator(*args) is True:
            self.from_str(*args)
        else:
            raise Exception(
                f"Unable to intialize Coordinates instance. kwargs must fully satisfy one of the following:\n\
                    (1) decimal kwargs: {expected_decimal_kwargs}, \n\
                    (2) or, DMS kwargs: {expected_dms_kwargs}, \n\
                    (3) or, a single positional argument of type str."
            )

    @classmethod
    def _init_kwarg_validator(cls, expected_kwargs, **kwargs):
        '''Check if kwargs has all the expected_kwargs.'''
        for k in expected_kwargs:
            if k not in kwargs:
                return False
        return True

    @classmethod
    def _init_args_validator(cls, *args):
        '''Check if args has a single str argument'''
        return len(args) == 1 and isinstance(args[0], str)

    def __str__(self) -> str:
        return f"{self.lat}, {self.long}"

    def __repr__(self):
        return f"Coordinates(lat={self.lat}, long={self.long})"

    def __eq__(self, other):
        return self.lat == other.lat and self.long == other.long

    @classmethod
    def _dms_to_decimal(cls, degree, minute, second):
        '''Convert DMS parts to decimal.'''
        return round(degree + minute / 60 + second / 3600, cls.precision)

    @classmethod
    def _validate(cls):
        '''
        validate data members
        '''

    def to_decimals(self) -> Tuple[float, float]:
        '''
        Get decimal representation.
        '''
        if self.lat is None or self.long is None:
            raise Exception("Not instantiated.")
        return round(self.lat, self.precision), round(self.long, self.precision)

    def to_dms(self) -> str:
        '''Get DMS representation.'''
        return f"{self.lat_degree}°{self.lat_minute}'{(self.lat_second)}\"{self.s_n} {self.long_degree}°{self.long_minute}'{self.long_second}\"{self.e_w}"

    def _internal_update_decimals(self):
        '''
        Updates internal decimal values using internal DMS parts.
        '''
        self.lat = self._dms_to_decimal(self.lat_degree, self.lat_minute, self.lat_second)
        self.long = self._dms_to_decimal(self.long_degree, self.long_minute, self.long_second)

        if self.s_n == Direction.SOUTH:
            self.lat *= -1
        if self.e_w == Direction.WEST:
            self.long *= -1

        self._validate()

    def _internal_update_dms(self):
        '''
        Updates internal DMS parts using internal decimals.
        '''
        coor_str = f"{self.lat},{self.long}"
        self.from_str(coor_str)
        self._validate()

    def from_str(self, *args, raise_exception=True):
        '''
        Instantiate Coordinates from string.
        '''
        parser = LatLongStringParser()
        parts = parser.parse(args[0])
        if parts:
            self.lat_degree, self.lat_minute, self.lat_second, self.s_n,\
                self.long_degree, self.long_minute, self.long_second, self.e_w = parts
            self.lat_second = round(self.lat_second, self.precision)
            self.long_second = round(self.long_second, self.precision)
            self._internal_update_decimals()
        elif raise_exception is True:
            raise Exception(f"Failed to parse string to coordinates: {args[0]}")

    def from_dms(self, lat_degree: int, lat_minute: int, lat_second: Union[int, float], south_north: Direction,
                 long_degree: int, long_minute: int, long_second: Union[int, float], east_west: Direction):
        '''Instantiate from DMS.'''
        self.lat_degree = lat_degree
        self.lat_minute = lat_minute
        self.lat_second = lat_second
        self.s_n = south_north
        self.long_degree = long_degree
        self.long_minute = long_minute
        self.long_second = long_second
        self.e_w = east_west
        self._internal_update_decimals()

    def from_decimals(self, lat, long):
        '''
        Instantiate Coordinates from decimal format latitude and longitude.
        '''
        self.lat = lat
        self.long = long
        self._internal_update_dms()
