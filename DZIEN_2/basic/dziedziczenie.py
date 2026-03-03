class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

class Manager(Employee):

    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus

    def get_salary(self):
        return self.salary + self.bonus

e = Employee("Anna",5600)
m = Manager("John",6000,1000)
print(e.get_salary())
print(m.get_salary())
