from enum import Enum


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    def to_coord(self, factor=100):
        match self:
            case Direction.UP:
                return 0, -1 * factor
            case Direction.RIGHT:
                return 1 * factor, 0
            case Direction.DOWN:
                return 0, 1 * factor
            case Direction.LEFT:
                return -1 * factor, 0
