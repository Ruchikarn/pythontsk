import math


class Employee:
    def __init__(self, salary, address):
        self.address = address
        self.salary = salary

    def calculate_tax(self):
        return 0.01 * self.salary


class Manager(Employee):
    def __init__(self, address, salary, department):
        self.department = department
        super().__init__(salary, address)

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


#

class Customer:
    def __init__(self, name, address, balance, account_type):
        self.name = name
        self.address = address
        self.__balance = balance
        self.account_type = account_type

    def deposit(self, amount):   # deposit, withdraw, print__balance are member functions as they are private.
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
        else:
            print('Insufficient balance')

    def print_balance(self):
        print(self.__balance)


John = Customer('John Doe', 'Tinkune', 900000, 'Saving')
# print(John.__balance)
John.deposit(10000)
John.print_balance()
# print(John.__balance)
#John.__balance = 0
# print(John.__balance)
