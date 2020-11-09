from src.project.Calculator import Calculator
from src.project.StatsCalculator import StatsCalculator
import math
from src.project.helper import Helper
from src.project.RandomCalculator import RandomCalculator

class SampleCalculator(StatsCalculator):

    @Helper.validateNumberInput
    def cohran(self,zScore, p, e):
        '''
        Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)
        :param zScore:
        :param p: probability of Sample
        :param e:margin of error
        :return: Sample Size
        '''
        return math.ceil((self.square(zScore) * p *(1-p))/self.square(1-e))

    def smapleSize(self,W, cL, p):
        # with unknown standard devation
        pass

    @Helper.validateNumberInput
    def marginOfError(self,populationSize, populationPortion,z_score):
        '''
        Find Margin of Error
        :param populationSize:
        :param populationPortion:
        :param z_score:
        :return: margin of error
        '''
        result = (populationPortion * (1-populationPortion))/populationSize
        return z_score * self.sqrt(result)


    @Helper.validateNumberInput
    def confidenceIntervalSmaple(self,mean,numberofObservation, std, zscore):
        '''
        Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)
        :param mean:
        :param numberofObservation:
        :param std:
        :param zscore:
        :return: tuple containing low bound and upper bound of confidenceInterval
        '''
        lower =  mean - (zscore* (std/ self.sqrt(numberofObservation)))
        high = mean + (zscore* (std/ self.sqrt(numberofObservation)))
        return  (lower,high)

    def simpleRandomSampling(self,size,lst):
        '''
        Simple random sampling
        :param size:
        :param lst:
        :return: size
        '''
        return RandomCalculator().selectRandomNList(lst,size)


    def confidenceInterval(self, width, p, zscore):
        '''
        Confidence Interval For a Sample
        :param width:
        :param p:
        :param zscore:
        :return:  Confidence Interval
        
        '''
        if width > 1 or p > 1:
            raise ValueError("Confidence interval cannot bigger than 1")
        q = 1- p
        E = width/ 2
        pq = p * q
        zAlpha = zscore / E
        answer = pq * self.square(zAlpha)
        return answer
