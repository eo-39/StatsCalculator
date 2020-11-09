from unittest import TestCase,skip
from src.project.SampleCalculator import SampleCalculator


class TestSampleCalculator(TestCase):
    @classmethod
    def setUpClass(self):
        self.smapleCalculator = SampleCalculator()

    @classmethod
    def tearDownClass(self):
        if self.smapleCalculator is not None:
            self.smapleCalculator = None

    def test_cohran(self):
        result =  self.smapleCalculator.cohran(1.96,0.5,0.95)
        self.assertAlmostEqual(result,385)

    def test_string_input(self):
        with self.assertRaises(ValueError):
            result = self.smapleCalculator.cohran("1.96", "0.5","0.95")
        with self.assertRaises(ValueError):
            result = self.smapleCalculator.marginOfError("1.96", "0.5","0.95")
        with self.assertRaises(ValueError):
            result = self.smapleCalculator.confidenceIntervalSmaple('0.9','0.8','0.6')
    def test_marginOfError(self):
        result = self.smapleCalculator.marginOfError(1000, 0.5,1.96)
        self.assertAlmostEqual(result,0.03099,places=3)

    def test_confidenceIntervalSmaple(self):
        result = self.smapleCalculator.confidenceIntervalSmaple(70,50,5,1.96)
        self.assertAlmostEqual(result[0], 68.6, places=1)
        self.assertAlmostEqual(result[1], 71.4, places=1)

    def test_simpleRandomSampling(self):
        result = self.smapleCalculator.simpleRandomSampling(10,[3, 8, 11, 17, 19,8, 12, 13, 17, 20])
        self.assertEqual(len(result),10)

    def test_confidenceInterval(self):
        result = self.smapleCalculator.confidenceInterval(0.06,0.41,1.96)
        self.assertAlmostEqual(result, 1032.53671, places=2)
