import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point( %d , %d )' % (self.x, self.y)


a = Point(4, 5)

print(a)

b = Point(5, 7)

distance = math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
print('Distance between a and b is', distance)
