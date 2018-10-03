class Employee:
    name = None
    married = None
    yearly_salary = None
    address = None

    def calculate_tax(self):
        if self.married == True and self.yearly_salary > 450000:
            taxable_amount = self.yearly_salary - 450000
            return taxable_amount * 0.15
        elif self.married == False and self.yearly_salary > 350000:
            taxable_amount = self.yearly_salary - 350000
            return taxable_amount * 0.15
        else:
            return self.yearly_salary * 0.01


ram = Employee()
ram.name = 'Ram Yadav'
ram.married = True
ram.yearly_salary = 500000
ram.address = 'Dharan'

print('Tax amount for emp is', ram.calculate_tax())
