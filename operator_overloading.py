class Time:
    def __init__(self, hr, m, sec):
        self.hr = hr
        self.min = m
        self.sec = sec

    def __str__(self):
        return '%d hr %d min %d sec' % (self.hr, self.min, self.sec)

    def __add__(self, other):
        sec = self.sec + other.sec

        if sec >= 60:
            minute = self.min + other.min + 1
            sec -= 60
        else:
            minute = self.min + other.min

        if minute >= 60:
            hr = self.hr + other.hr + 1
            minute -= 60
        else:
            hr = self.hr + other.hr

        return Time(hr, minute, sec)

    def __sub__(self, other):
        pass


a = Time(10, 35, 40)
b = Time(2, 45, 5)
c = a - b
print(c)
