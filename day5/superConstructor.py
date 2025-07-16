class Parent:
    def __init__(self):
        print("Parent constructor called")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor called")


c = Child()
