import math

class Shape:
    pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __int__(self):
        return self.area()

    def __str__(self):
        return f"Rectangle: Width = {self.width}, Height = {self.height}"

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def __int__(self):
        return int(self.area())  # Перетворення площі у ціле число

    def __str__(self):
        return f"Circle: Radius = {self.radius}"

    def area(self):
        return math.pi * self.radius ** 2

rect = Rectangle(4, 5)
circle = Circle(3)

print("Int of Rectangle:", int(rect))
print("Int of Circle:", int(circle))
print("String of Rectangle:", str(rect))
print("String of Circle:", str(circle))