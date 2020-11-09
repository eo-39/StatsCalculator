from Calculator.Calculator import Calculator
from Statistics.Mean import get_mean
from Statistics.Median import get_median
from Statistics.Mode import get_mode
from Statistics.Variance import get_variance
from Statistics.StandardDeviation import get_standard_deviation
from Statistics.ZScore import get_z_score


class Statistics(Calculator):

    def __init__(self):
        pass

    def stats_mean(self, data):
        self.result = get_mean(data)
        return self.result

    def stats_median(self, data):
        self.result = get_median(data)
        return self.result

    def stats_mode(self, data):
        self.result = get_mode(data)
        return self.result

    def stats_variance(self, data):
        self.result = get_variance(data)
        return self.result

    def stats_standard_deviation(self, data):
        self.result = get_standard_deviation(data)
        return self.result

    def stats_z_score(self, data):
        self.result = get_z_score(data)
        return self.result
