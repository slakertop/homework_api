from src.Figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, radius):
        self.name = 'Circle'
        self.radius = radius

    @property
    def get_area(self):
        return pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * pi * self.radius
