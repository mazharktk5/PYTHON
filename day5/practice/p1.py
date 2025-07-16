class TwoDVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"({self.x}, {self.y})")
        


class ThreeDVector(TwoDVector):
    def __init__(self, x, y,z):
         super().__init__(x,y)
         self.z = z
    def show(self):
        print(f"({self.x}, {self.y}, {self.z})")



a = TwoDVector(3,5)
a.show()
b = ThreeDVector(3,5,7)
b.show()