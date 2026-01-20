class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super(). __init__ (name, salary)
        self.bonus = bonus

    def calculate_pay(self):
        return self.salary + self.bonus
    
Employee = Employee("john",500000)
Manager = Manager("collins",790000,200000)

print(Employee.calculate_pay())
print(Manager.calculate_pay())