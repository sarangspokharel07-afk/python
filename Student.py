class Student:

    def __init__(self, name, ID, roll_number):
        self.name = name
        self.ID = ID
        self.roll_number = roll_number

alex = Student("Alex", 1, 11)
rohan = Student("Rohan", 2, 12)
sameer = Student("Sameer", 3, 13)

print(alex.name, alex.ID, alex.roll_number)
print(rohan.name, rohan.ID, rohan.roll_number)
print(sameer.name, sameer.ID, sameer.roll_number)