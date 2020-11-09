import unittest

from RandomGen.RandomRange import randDec
from RandomGen.RandomRange import randInt
from RandomGen.RandomList import randDecList
from RandomGen.RandomList import randIntList
from RandomGen.SelectRandom import selectRand


class MyTestCase(unittest.TestCase):

    def test_randomInt_generator(self):
        num = randInt(0, 100)
        self.assertIs(type(num), int)
        # print(num)

    def test_randomDec_generator(self):
        num = randDec(0, 100)
        self.assertIs(type(num), float)
        # print(num)

    def test_randomIntList_generator(self):
        datalist = randIntList(5, 0, 100)
        self.assertIs(type(datalist[1]), int)
        # print(datalist)
        datalist.clear()

    def test_randomDecList_generator(self):
        datalist = randDecList(5, 0, 100)
        self.assertIs(type(datalist[1]), float)
        # print(datalist)
        datalist.clear()

    def test_selectRandom_generator(self):
        datalist = randIntList(5, 0, 100)
        # Select random element
        singlerandom = selectRand(datalist)
        self.assertIs(type(singlerandom), int)
        # Select N random elements
        randomlist = selectRand(datalist, 2)
        self.assertIs(type(randomlist), list)
        datalist.clear()



if __name__ == '__main__':
    unittest.main()