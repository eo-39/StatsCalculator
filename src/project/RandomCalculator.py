from src.project.Calculator import Calculator
import random
from src.project.helper import Helper
class RandomCalculator(Calculator):
    @Helper.validateNumberInput
    def generateRandomNumber(self,low,high):
       '''
       Generate a random number without a seed between a range of two numbers
       :param low: low bound of the random number
       :param high: high bound of the random number
       :return: a random number
       '''
       return random.randrange(low,high)

    @Helper.validateNumberInput
    def generateRandomSeedNumber(self,seed,low,high):
        '''
        Generate a random number with a seed between a range of two numbers
        :param seed: the seed
        :param low: low bound of the random number
        :param high: high bound of the random number
        :return: a random number with seed
        '''
        random.seed(seed)
        return random.randrange(low,high)

    @Helper.validateNumberInput
    def generateRandomList(self,n,low,high):
        '''
        Generate a list of N random numbers with a seed and between a range of number
        :param n: Number of List needs to be generated
        :param low: low bound of the random list
        :param high: high bound of the random list
        :return: random list
        '''
        return [random.randrange(low,high) for x in range(n)]

    @Helper.validateListInput
    def selectRandomFromList(self,lst):
        '''
        Select a random item from a list
        :param lst: list to be selected
        :return: chosen number
        '''
        return random.choice(lst)

    @Helper.validateListInput
    def selectRandomwithSeed(self,lst):
        '''
        Set a seed and randomly.select the same value from a list
        :param lst:
        :return: chosen number
        '''
        random.seed(1)
        return random.choice(lst)

    def selectRandomNList(self,lst,n):
        '''
        Select N number of items from a list without a seed
        :param lst:
        :param n:
        :return: list of randomly chosen number
        '''
        return random.sample(lst,n)

    def selectRandomNListSeed(self,lst,n,seed):
        '''
        Select N number of items from a list with a seed
        :param lst:
        :param n:
        :param seed:
        :return: list of randomly chosen number
        '''
        random.seed(seed)
        return random.sample(lst, n)


