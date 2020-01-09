from dlgo import Point

class Move():
    def __init__(self, point:Point = None, is_pass: bool = False, is_resign: bool = False):
        self.point = point
        self.is_play =  (self.point is not None)
        self.is_pass = is_pass
        self.is_resign = is_resign

    @classmethod
    def play(cls, point:Point):
        return Move(point=point)

    @classmethod
    def pass_turn(cls):
        return Move(is_pass=True)

    @classmethod
    def resign(cls):
        return Move(is_resign=True)

