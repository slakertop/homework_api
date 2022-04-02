from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_one, side_two):
        self.name = 'Rectangle'
        self.side_one = side_one
        self.side_two = side_two

    @property
    def get_area(self):
        return self.side_one * self.side_two

    @property
    def perimeter(self):
        return 2 * (self.side_one + self.side_two)
