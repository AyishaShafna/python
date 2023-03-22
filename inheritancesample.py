class A:
    def __init__(self):
        print("Parent class A")

    def display1(self):
        print("class A display1")

    def display2(self):
        print("class A display2")

    def display3(self):
        print("class A display3")

    

class B(A):
    def __init__(self):
        super().__init__()
        print("child class B")
    
    def display3(self):
        print("class B display4")

class C(B):
    def __init__(self):
        super().__init__()
        print("child class C")

    def display5(self):
        print("class C display5")    
    

a = B().display3()