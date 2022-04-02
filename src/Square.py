from src.Figure import Figure


class Square(Figure):
    def __init__(self, side):
        self.name = 'Square'
        self.side = side

    @property
    def get_area(self):
        return self.side * self.side

    @property
    def perimeter(self):
        return 4 * self.side
