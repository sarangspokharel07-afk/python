class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

harry = Employee("Harry", 10000)
rohan = Employee("Rohan", 20000)
sita = Employee("Sita", 30000)

print(harry.name, harry.salary)
print(rohan.name, rohan.salary)
print(sita.name, sita.salary)