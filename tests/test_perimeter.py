from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle


def test_square_area():
    square = Square(10)
    assert square.perimeter == 40


def test_circle_area():
    circle = Circle(10)
    assert circle.perimeter == 62.83185307179586


def test_triangle_area():
    triangle = Triangle(10, 10, 9)
    assert triangle.perimeter == 29


def test_rectangle_area():
    rectangle = Rectangle(10, 15)
    assert rectangle.perimeter == 50
