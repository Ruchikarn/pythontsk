import math

# OOP is mainly used in real world mapping
class Point:
    x = None
    y = None

a = Point()
a.x = 5
a.y = 3

b = Point()

b.x = 7
b.y = 10


distance = math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
print(distance)
print(type(a))

#

class Point:
    x = None
    y = None

    def quadrant(self):

        if self.x == 0 or self.y == 0:
            return None
        if self.x > 0 and self.y > 0:
            return 1
        if self.x < 0 and self.y > 0:
            return 2
        if self.x < 0 and self.y < 0:
            return 3
        if self.x > 0 and self.y < 0:
            return 4


a = Point()
a.x = 5
a.y = 3

b = Point()

b.x = 7
b.y = 10


c = Point()
c.x = -7
c.y = -8

d = Point()
d.x = -4
d.y = 4

e = Point()
e.x = 5
e.y = -5

f = Point()
f.x = 0
f.y = 0

print('a is in', a.quadrant(), 'quadrant')
print('b is in', b.quadrant(), 'quadrant')
print('c is in', c.quadrant(), 'quadrant')
print('d is in', d.quadrant(), 'quadrant')
print('e is in', e.quadrant(), 'quadrant')
print('f is in', a.quadrant(), 'quadrant')

