import unittest
from src.project.RandomCalculator import  RandomCalculator

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.rc = RandomCalculator()

    @classmethod
    def tearDownClass(self):
        if self.rc is not None:
            self.rc = None

    def test_generateRandomNumber_string_to_throw(self):
        with self.assertRaises(ValueError):
            self.rc.generateRandomNumber("1","2")
    def test_generateRandomNumber(self):
        result = self.rc.generateRandomNumber(10,20)
        print(f"result: {result}")
        self.assertEqual(result >=10 and result<= 20, True)

    def test_generateRandomSeedNumber(self):
        result = self.rc.generateRandomSeedNumber(10,10,20)
        result2 = self.rc.generateRandomSeedNumber(10,10,20)
        self.assertEqual(result,result2)
    def test_generateRandomList(self):
        result = self.rc.generateRandomList(9,10,20)
        self.assertEqual(len(result), 9)
        self.assertEqual(all([x <= 20 and x >= 10  for x in result]),True)

    def test_selectRandomFromList(self):
        result = self.rc.selectRandomFromList([1,2,4,5])
        self.assertEqual(result in [1,2,4,5], True)
    def test_selectRandomwithSeed(self):
        result = self.rc.selectRandomwithSeed([1,2,4,5])
        result2 = self.rc.selectRandomwithSeed([1,2,4,5])
        self.assertEqual(result,result2)
    def test_selectRandomNList(self):
        result = self.rc.selectRandomNList([3, 8, 11, 17, 19,8, 12, 13, 17, 20],3)
        self.assertEqual(len(result),3)
    def test_selectRandomNListSeed(self):
        result = self.rc.selectRandomNListSeed([3, 8, 11, 17, 19, 8, 12, 13, 17, 20], 3,4)
        result2 = self.rc.selectRandomNListSeed([3, 8, 11, 17, 19, 8, 12, 13, 17, 20], 3,4)
        self.assertCountEqual(result,result2)



if __name__ == '__main__':
    unittest.main()
