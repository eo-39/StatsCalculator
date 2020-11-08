import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


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

        filepath = './Tests/Data/Unit Test Addition.csv'
        csv_data = self.datafile.csv(filepath)
        for row in csv_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
        csv_data.clear()

    def test_subtraction_method_calculator(self):
        filepath = './Tests/Data/Unit Test Subtraction.csv'
        csv_data = self.datafile.csv(filepath)
        for row in csv_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
        csv_data.clear()

    def test_multiplication_method_calculator(self):
        filepath = './Tests/Data/Unit Test Multiplication.csv'
        csv_data = self.datafile.csv(filepath)
        for row in csv_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
        csv_data.clear()

    def test_division_method_calculator(self):
        filepath = './Tests/Data/Unit Test Division.csv'
        csv_data = self.datafile.csv(filepath)
        for row in csv_data:
            self.assertEqual(self.calculator.divide(row['Value 2'], row['Value 1']), float(row['Result']))
        csv_data.clear()

    def test_square_method_calculator(self):
        filepath = './Tests/Data/Unit Test Square.csv'
        csv_data = self.datafile.csv(filepath)
        self.assertEqual(self.calculator.divide(5, 0), 1)
        for row in csv_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            csv_data.clear()

    def test_square_root_method_calculator(self):
        filepath = './Tests/Data/Unit Test Square Root.csv'
        csv_data = self.datafile.csv(filepath)
        for row in csv_data:
            self.assertEqual(self.calculator.square_root(row['Value 1']), float(row['Result']))
            csv_data.clear()

if __name__ == '__main__':
    unittest.main()
