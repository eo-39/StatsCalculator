from Calculator.Addition import  addition
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Divison import division
from Calculator.Squared import squared
from Calculator.SquareRoot import square_root
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Variance import variance
from Statistics.StandardDev import stddev
from Statistics.Zscore import zscore

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
        self.result = square_root(a)
        return self.result

    def mean(self, a):
        self.result = mean(a)
        return self.result

    def median(self, a):
        self.result = median(a)
        return self.result

    def mode(self, a):
       self.result = mode(a)
        return self.result

    def variance(self, a):
       self.result = variance(a)
       return self.result

    def stddev(self, a):
       self.result = stddev(a)
       return self.result

    def zscore(self, a):
        self.result = zscore(a)
        return self.result
