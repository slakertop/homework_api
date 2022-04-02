from math import pi


class Ball:
    def __init__(self):
        self.area = 100
        self.perimeter = 200

    @property
    def get_area(self):
        return self.area()

    @property
    def perimeter(self):
        return self.perimeter()
