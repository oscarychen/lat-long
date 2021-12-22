from enum import Enum


class Direction(Enum):
    SOUTH = 'S'
    NORTH = 'N'
    EAST = 'E'
    WEST = 'W'

    def __str__(self) -> str:
        return f"{self.value}"
