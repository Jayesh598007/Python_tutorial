#  Create a class calculator, capable of finding square, cube, and squareroot of a number

class calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The square of {self.number} is {self.number **2}")

    def squareroot(self):
        print(f"The squareroot of {self.number} is {self.number **0.5} ")

    def cube(self):
        print(f"The square of {self.number} is {self.number **3}")


Value = int(input("Enter the value:"))
a = calculator(Value)
a.square()
a.squareroot()
a.cube()
