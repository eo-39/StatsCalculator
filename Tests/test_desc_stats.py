import unittest
from src.project.Calculator import Calculator
from src.project.StatsCalculator import StatsCalculator

class TestDescriptiveStatistics(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.calculator = Calculator()
        self.statsCalculator = StatsCalculator()

    @classmethod
    def tearDownClass(self):
        if self.calculator is not None or self.statsCalculator is not None:
            self.calculator = None
            self.statsCalculator = None

    def test_isinstanceOf_calculator(self):
        self.assertEqual(issubclass(StatsCalculator,Calculator),True,"Stats Calculator is not subclass of Calculator")

    def test_string_input(self):
        with self.assertRaises(ValueError):
            result = self.statsCalculator.mean(["hello","",""])

    def test_mean(self):
        result = self.statsCalculator.mean((1,2,3))
        self.assertAlmostEqual(result,2)

    def test_mean_invalid_input(self):
        with self.assertRaises(ValueError):
            result = self.statsCalculator.mean(['1','2'])
    def test_mean_not_empty_list(self):
        with self.assertRaises(ValueError):
            result = self.statsCalculator.mean([])


    def test_mean_invalid_input(self):
        with self.assertRaises(ValueError):
            self.statsCalculator.mean([1,'o',3])


    def test_median_value(self):
        result = self.statsCalculator.median([7,9,12,13,14,15])
        self.assertAlmostEqual(result,12.5,"tests median")


    def test_mode_value(self):
        result = self.statsCalculator.mode([10, 12, 23, 23, 16, 23, 21, 16])
        self.assertAlmostEqual(result,23,"Mode tests")

    def test_mean_Dev(self):
        test_result =  self.statsCalculator.stdev([7,9,12,13,14,15])
        self.assertAlmostEqual(test_result,2.808716591)

    def test_z_score(self):
        test_result = self.statsCalculator.z_score(11,[7,9,12,13,14,15])
        self.assertAlmostEqual(test_result,-0.23735,places=2)

if __name__ == '__main__':
    unittest.main()
