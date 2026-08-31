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
        super().skills()
        super().skills1()
        super().skills2()
        print("Coding")
    
    

c=Child()
c.skills3()
