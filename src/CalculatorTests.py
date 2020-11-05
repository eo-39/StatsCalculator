import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()
        self.datafile = CsvReader()

    def test_instantiate_calculator(self):

        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):

        self.assertEqual(self.calculator.result, 0)

    def test_instantiate_parser(self):
        self.assertIsInstance(self.datafile, CsvReader)

    def test_add_method_calculator(self):

        filepath = './src/Unit Test Addition.csv'
        csv_data = self.datafile.csv(filepath)
        for row in csv_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
        csv_data.clear()

    def test_subtraction_method_calculator(self):
        filepath = './src/Unit Test Subtraction.csv'
        csv_data = self.datafile.csv(filepath)
        for row in csv_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
        csv_data.clear()

    def test_multiplication_method_calculator(self):
        filepath = './src/Unit Test Multiplication.csv'
        csv_data = self.datafile.csv(filepath)
        for row in csv_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
        csv_data.clear()

    def test_division_method_calculator(self):
        filepath = './src/Unit Test Division.csv'
        csv_data = self.datafile.csv(filepath)
        for row in csv_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
        csv_data.clear()

    def test_square_method_calculator(self):
        filepath = './src/Unit Test Square.csv'
        csv_data = self.datafile.csv(filepath)
        for row in csv_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            csv_data.clear()

    def test_square_root_method_calculator(self):
        filepath = './src/Unit Test Square Root.csv'
        csv_data = self.datafile.csv(filepath)
        for row in csv_data:
            self.assertEqual(self.calculator.square_root(row['Value 1']), float(row['Result']))
            csv_data.clear()

if __name__ == '__main__':
    unittest.main()
