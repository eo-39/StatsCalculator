import random


class RandomGenerator:
    result = 0

    def __init__(self):
        pass

    # Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
    def generate_rand_num_by_range_wo_seed(self, low, high):
        self.result = random.uniform(low, high)
        return self.result

    # Generate a random number with a seed between a range of two numbers - Both Integer and Decimal
    def generate_rand_num_by_range_w_seed(self, seed, version, low, high):
        random.seed(seed, version)
        self.result = random.uniform(low, high)
        return self.result

    # Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
    def get_rand_num_list_by_range_w_seed(self, size, seed, version, low, high):
        random.seed(seed, version)
        try:
            self.result = random.sample(range(low, high), size)
        except ValueError:
            print('Sample size exceeded population size.')
        return self.result

    # Set a seed and randomly select the same value from a list
    def set_seed_and_get_rand_from_list(self, seed, version, number_list):
        random.seed(seed, version)
        self.result = random.choice(number_list)
        return self.result

    # Select a random item from a list
    def get_rand_item_from_list(self, number_list):
        self.result = random.choice(number_list)
        return self.result

    # Select N number of items from a list without a seed
    def get_rand_num_list_wo_seed(self, size, number_list):
        try:
            self.result = random.sample(number_list, size)
        except ValueError:
            print('Sample size exceeded population size.')
        return self.result

    # Select N number of items from a list with a seed
    def get_rand_num_list_w_seed(self, size, seed, version, number_list):
        random.seed(seed, version)
        try:
            self.result = random.sample(number_list, size)
        except ValueError:
            print('Sample size exceeded population size.')
        return self.result
