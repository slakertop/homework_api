from src.Figure import Figure
from math import sqrt


class Triangle(Figure):
    def __init__(self, one_side, second_side, third_side):
        self.name = 'Triangle'
        self.one_side = one_side
        self.second_side = second_side
        self.third_side = third_side

    @property
    def get_area(self):
        p = (self.one_side + self.second_side + self.third_side) / 2
        return sqrt(p * (p - self.one_side) * (p - self.second_side) * (p - self.third_side))

    @property
    def perimeter(self):
        return self.one_side + self.second_side + self.third_side
