import math


class Employee:
    def calculate_tax(self):
        return 0.01 * self.salary


class Manager(Employee):
    def __init__(self, address, salary, department):
        self.address = address
        self.salary = salary
        self.department = department

    def assign_task(self):
        print('Task Assigned!')


emp = Manager('Baneswor', 300000, 'Physics')
print(emp.calculate_tax())
print(emp.assign_task())


#
class Teacher(Employee):
    def __init__(self, address, fulltime, salary, subject):
        self.address = address
        self.fulltime = fulltime
        self.salary = salary
        self.subject = subject

    def class_hour(self):
        if self.fulltime >= 9:
            print('Full-Time teacher')
        else:
            print('Part-Time Teacher')

    def take_class(self):
        print('He is a full time teacher')


tec = Teacher('Tinkune', 7, 80000000, 'Chemistry')
print(tec.calculate_tax())
print(tec.take_class())
print(tec.class_hour())


#
class Helper(Employee):
    def __init__(self, name, address, salary):
        self.name = name
        self.address = address
        self.salary = salary


    def helper_type(self):
        print('full time helper')


help = Helper('Joh', 'Nakkhu', 450000)
print(help.calculate_tax())
print(help.helper_type())
