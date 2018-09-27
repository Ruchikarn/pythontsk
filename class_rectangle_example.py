import math


class Rectangle:
    length = None
    breadth = None

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def square(self):
        if self.length == self.breadth:
            return self.length * self.length
        else:
            return self.length * self.breadth


sample_rect = Rectangle()
sample_rect.length = 3
sample_rect.breadth = 4
sample_rect.a = 2
sample_rect.b = 4
sample_rect.c = 3

print(sample_rect.area())

print(sample_rect.perimeter())
print(sample_rect.square())


#
class Triangle:
    a = None
    b = None
    c = None
    s = None

    def area(self):
        self.s = (self.a + self.b + self.c) / 2
        return math.sqrt(self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c))


sample_tri = Triangle()
sample_tri.a = 2
sample_tri.b = 4
sample_tri.c = 3
print(sample_tri.area())


#
class Circle:
    radius = None

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return math.pi * 2 * self.radius


sample_circ = Circle()
sample_circ.radius = 2

print(sample_circ.area())
print(sample_circ.circumference())


#
class Cube:
    length = None
    breadth = None
    height = None
    volume = None

    def area(self):
        self.volume = self.length * self.breadth * self.height
        return self.volume


sample_cube = Cube()
sample_cube.length = 2
sample_cube.breadth = 2
sample_cube.height = 2

print(sample_cube.area())


#
class Employee:
    age = None
    salary = None
    married = None

    tax = None

    def status(self):
        if self.salary >= 500000:
            self.tax = 0.15 * self.salary
            print('For Married employee')

        elif self.salary > 350000:
            self.tax = 0.15 * self.salary
            print('For unmarried employee')
        else:
            self.tax = 0.001 * self.salary
            print('default tax')


sample_emp = Employee()
sample_emp.salary = 200000

print(sample_emp.status())


#

class Employees:
    name = None
    married = None
    yearly_salary = None
    address = None

    def calculate_tax(self):
        if self.married == True and self.yearly_salary > 450000:
            taxable_amount = self.yearly_salary - 450000
            return taxable_amount * 0.15

        elif self.married == False and self.yearly_salary > 350000:
            taxable_amount = self.yearly_salary = 350000
            return taxable_amount * 0.15

        else:
            return self.yearly_salary * 0.01


sabba = Employees()
sabba.name = 'Sabba Malla'
sabba.married = False
sabba.yearly_salary = 500000
sabba.address = 'Kathmandu'
print('Tax amount for emp is', sabba.calculate_tax())
