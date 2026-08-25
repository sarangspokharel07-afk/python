#WAP to create a object name form and add all the details as a __init__() constructor print all the details

class Form:
    def __init__(self, name, age, email, phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

sarangs = Form("Sarangs", 20, "sarangs07@example.com", "1234567890")

print(sarangs.name, sarangs.age, sarangs.email, sarangs.phone)


