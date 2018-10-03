class Rectangle:
    length = None
    breadth = None

    def area(self):
        return self.length * self.breadth


sample_rect = Rectangle()

sample_rect.length = 3
sample_rect.breadth = 4

print(sample_rect.area())