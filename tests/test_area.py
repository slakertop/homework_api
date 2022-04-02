from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle


def test_square_area():
    square = Square(10)
    assert square.get_area == 100


def test_circle_area():
    circle = Circle(10)
    assert circle.get_area == 314.1592653589793


def test_triangle_area():
    triangle = Triangle(10, 10, 9)
    assert triangle.get_area == 40.18628497385644


def test_rectangle_area():
    rectangle = Rectangle(10, 15)
    assert rectangle.get_area == 150
