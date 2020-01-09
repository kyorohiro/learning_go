import enum

class Player(enum.Enum):
    black = 1
    white = 2

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white

import dataclasses
@dataclasses.dataclass
class Point:
    row: int
    col: int
    def neighbor(self):
        return [
            Point(self.row-1, self.col),
            Point(self.row+1, self.col),
            Point(self.row, self.col-1),
            Point(self.row, self.col+1),
        ]
import copy
from dlgo.gotypes import Player