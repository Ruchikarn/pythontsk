import math


class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def square(self):
        if self.length == self.breadth:
            return self.length * self.length
        else:
            return self.length * self.breadth


rect = Rectangle(3, 5)

sample_rect = Rectangle(5, 5)

print(sample_rect.area())

print(sample_rect.perimeter())
print(sample_rect.square())


#
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'Point(%d, %d)' % (self.x, self.y)

a = Point(4, 5)
print(type(a))
