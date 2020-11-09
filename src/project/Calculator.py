import math
from src.project.helper import Helper
class Calculator:
    @Helper.validateNumberInput
    def add(self,x,y):
        '''

        :param x:
        :param y:
        :return number:
        adding two number
        '''
        if type(x) not in (int, float) :
            raise ValueError('Value is not int or float')
        return x+y

    @Helper.validateNumberInput
    def minus(self,x,y):
        '''

        :param x:
        :param y:
        :return: number
        minus two number
        '''
        return y-x

    @Helper.validateNumberInput
    def multiply(self,x,y):
        '''

        :param x:
        :param y:
        :return: number
        Mutiply two number
        '''
        return x*y

    @Helper.validateNumberInput
    def divide(self,x,y):
        '''

        :param x:
        :param y:
        :return: number
        divide two number
        '''
        if y == 0:
            raise ValueError("Can't be divided by zero")
        return x/y

    @Helper.validateListInput
    def sumList(self,lst):
        '''
         sum the lists of numbers
        :param lst: list of number
        :return: sum of list of number
        '''
        result =0
        for x in range(0, len(lst)):
            result += lst[x]
        return result

    @Helper.validateNumberInput
    def square(self,x):
        '''
        Square a number
        :param x:
        :return: square of x
        '''
        return x**2

    @Helper.validateNumberInput
    def sqrt(self,x):
        '''
        Sqaure root of number
        :param x:
        :return:
        '''
        return math.sqrt(x)