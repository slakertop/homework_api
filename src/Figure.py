class Figure:
    def __init__(self, name, area):
        self.name = name
        self.get_area = area

    def add_area(self, second_figure):
        if not isinstance(second_figure, Figure):
            raise ValueError
        return self.get_area + second_figure.get_area
