from .Addition import  addition
from .Subtraction import subtraction
from .Multiplication import multiplication
from .Divison import division
from .Squared import squared
from .SquareRoot import square_root


class Calculator:
    result = 0

    def _init_(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)

        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self,a):
        self.result = squared(a)
        return self.result

    def square_root(self,a):
        self.result = square_root(a);
        return self.result