import unittest
import os
from src.project.Calculator import Calculator
from src.project.CsvReader import CsvReader
from parameterized import parameterized, parameterized_class

TEST_DIR = os.path.abspath('./src/test/testscase')

class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.calculator = Calculator()

    @classmethod
    def tearDownClass(self):
        if self.calculator is not None:
            self.calculator = None

    @parameterized.expand(CsvReader(TEST_DIR + '/Addition.csv').readFile())
    def test_add(self,a,b,expect_result):
        print("Calculator Class add testing")
        print( f'{int(a)} + {int(b)} = {int(expect_result)}')
        result = self.calculator.add(int(a) ,int(b))
        self.assertEqual(result, int(expect_result))
    def test_add_error(self):
        print("Calculator Class add testing")
        with self.assertRaises(ValueError):
            result = self.calculator.add('1','2')


    @parameterized.expand(CsvReader(TEST_DIR + '/Subtraction.csv').readFile())
    def test_subtract(self, a, b, expected_result):
        print(f"Substract Testing {self.calculator.minus.__name__}")
        print(f'{int(a)} - {int(b)} = {int(expected_result)}')
        result = self.calculator.minus(int(a), int(b))
        self.assertEqual(result, int(expected_result))

    @parameterized.expand(CsvReader(TEST_DIR + '/Division.csv').readFile())
    def test_divide(self, a, b, expected_result):
        print(f'{b} / {a} = {expected_result}')
        result = self.calculator.divide(float(b), float(a))
        self.assertAlmostEqual(result, float(expected_result))

    @parameterized.expand(CsvReader(TEST_DIR + '/Multiplication.csv').readFile())
    def test_multiply(self, a, b, expected_result):
        print(f'{a} * {b} = {expected_result}')
        result = self.calculator.multiply(int(b), int(a))
        self.assertEqual(result, int(expected_result))

    @parameterized.expand(CsvReader(TEST_DIR + '/Square.csv').readFile())
    def test_square(self, a, expected_result):
        print(f'{a} ^ 2 = {expected_result}')
        result = self.calculator.square(int(a))
        self.assertEqual(result, int(expected_result))
        print(f"Sqare test: {a}^2 ={expected_result}")

    @parameterized.expand(CsvReader(TEST_DIR + '/Square Root.csv').readFile())
    def test_sqrt(self,a,expected_result):
        print(f'{a} ^ -2 = {expected_result}')
        result = self.calculator.sqrt(int(a))
        self.assertAlmostEqual(result,float(expected_result))

    def test_sum_list(self):
        print(f' sumlist [1,2,3] ^ -2 = 6')
        result = self.calculator.sumList([1,2,3])
        self.assertEqual(result,6,"SumList:Test")
if __name__ == '__main__':
    unittest.main()
