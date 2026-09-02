#create a class (2D-vector)and use it to create another class representing a 3D-vector.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
       print(f"({self.x}i+{self.y}j)")

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print(f"({self.x}i+{self.y}j+{self.z}k)")

v=Vector3D(1, 2, 3)
v.show()    