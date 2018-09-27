import math


class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%d : %d : %d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        second = self.second + other.second
        if second >= 60:
            second = self.second + other.second + 1
            second -= 60

        else:
            minute = self.minute + other.minute

        if minute >= 60:
            hour = self.hour + other.hour + 1
            minute = minute - 60
        else:
            hour = self.hour + other.hour
        return Time(hour, minute, second)


a = Time(10, 33, 40)
b = Time(2, 30, 5)
c = a + b
print(a)
print(b)
print(c)


#

class Height:
    def __init__(self, foot, inch):
        self.foot = ft
        self.inch = inch

    def __str__(self):
        return '%d : %d : %d' % (self.foot, self.inch)

    def __sub__(self, other):
        inch = self.inch + other.inch

        if inch >= 12:
            foot = self.inch + other.inch + 1

        else:
            foot = self.foot + other.foot

        return Height(foot, inch)


a = Height(6, 5)
b = Height(6, 12)

print(a)
print(b)
