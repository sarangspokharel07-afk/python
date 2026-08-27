class Grandfather:

    def house(self):
        print("Grandfather has a house.")

class Father(Grandfather):
    def car(self):
        print("Father has a car.")

class Son(Father):
    def bike(self):
        print("Son has a bike.")

me=Father()
me.house()
me.car()

