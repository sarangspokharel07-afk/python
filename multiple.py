class Grandfather:

    def skills(self):
        print("Gardening")


class Father:

    def skills1(self):
        print("Driving")

class Mother:

    def skills2(self):
        print("Cooking")        
    
class Child(Father, Mother, Grandfather):

    def skills3(self):
        print("Coding")

c=Child()
c.skills()
c.skills1()
c.skills2()
c.skills3()