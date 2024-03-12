import math
import turtle

class Circle:
    def __init__(self, value_error=None, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
            self.diameter = 2 * radius
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("Please specify either radius or diameter.")

    def get_area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"The radius of the circle is {self.radius}, and the diameter is {self.diameter}"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=(self.radius + other.radius))
        else:
            raise ValueError(f"Cannot add circle")

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.get_area() < other.get_area()
        else:
            raise ValueError(f"Cannot compare circle")

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.get_area() == other.get_area()
        else:
            raise ValueError(f"Cannot compare circle")

    @classmethod
    def sort_circles_by_area(cls, circles):
        sorted_circles = sorted(circles, key=lambda circle: circle.get_area())
        print("Sorted circles:")
        for circle in sorted_circles:
            print("Radius:", circle.radius, "| Diameter:", circle.diameter, "| Area:", circle.get_area())
        return sorted_circles

    @classmethod
    def draw_circles(cls, circles):
        t = turtle.Turtle()
        for idx, circle in enumerate(Circle.sort_circles_by_area(circles)):
            t.penup()
            t.goto(0, -idx * 100)
            t.pendown()
            t.circle(circle.radius)

        turtle.done()


circle1 = Circle(radius=120)
circle2 = Circle(diameter=200)
circle3 = Circle(radius=50)
print(circle1.diameter)
print(circle2.radius)
print(circle1.get_area())
print(circle1)
print(circle1 + circle2)
print(circle1 < circle2)
print(circle1 == circle3)

Circle.sort_circles_by_area([circle1, circle2, circle3])

Circle.draw_circles([circle1, circle3])


