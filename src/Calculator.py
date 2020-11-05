import math

def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c

def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c

def multiplication(a,b):
    a = int(a)
    b = int(b)
    c = a * b
    return c

def division(a,b):
    a = float(a)
    b = float(b)
    c = round(b / a, 9)
    return c

def squared(a):
    a = int(a)
    b = a * a
    return b

def square_root(a):
        return round(math.sqrt(float(a)), 9)

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