class Parent:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"hello, my name is {self.name}.")

class Child1(Parent):
    def play(self):
        print(f"{self.name} is playing.")

class Child2(Parent):
    def study(self):
        print(f"{self.name} is studying.")

child1 = Child1("Dave")
child2 = Child2("Eve")

child1.greet()
child1.play()

child2.greet()
child2.study()