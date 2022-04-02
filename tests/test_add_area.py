from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Ball import Ball
import pytest


def test_add_circle_square_areas():
    circle = Circle(10)
    square = Square(10)
    print(circle.get_area)
    print(square.get_area)
    print(circle.add_area(square))
    assert circle.add_area(square) == circle.get_area + square.get_area


def test_add_rectangle_triangle_areas():
    rectangle = Rectangle(10, 15)
    triangle = Triangle(5, 6, 7)
    assert rectangle.add_area(triangle) == triangle.get_area + rectangle.get_area


@pytest.mark.negative
def test_add_circle_ball_areas():
    circle = Circle(10)
    ball = Ball()
    assert circle.add_area(ball) == circle.get_area + ball.area


@pytest.mark.negative
def test_add_circle_number_areas():
    circle = Circle(10)
    number = 100
    assert circle.add_area(number) == circle.get_area + number
