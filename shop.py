#WAP to using inheritance of a father and son father has a shop name
#Sharma Shop which inheritane to son and become sharman shop and son

class Father:

    def __init__(self):
         self.shop_name = "Sharma gitShop"


class Son(Father):

    def __init__(self):
         super().__init__()
         self.shop_name = "& Sons"

s=Son()
print(s.shop_name)