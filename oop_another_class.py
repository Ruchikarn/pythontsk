class Customer:
    def __init__(self, name, balance, address, account_type):
        self.name = name
        self.__balance = balance
        self.address = address
        self.account_type = account_type

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
        else:
            print('Insufficient Balance')

    def print_balance(self):
        print(self.__balance)


john = Customer('John Doe', 80000, 'Tinkune', 'Saving')

# print(john.__balance)

john.deposit(10000)

john.print_balance()

# john.__balance = 0

# print(john.balance)
