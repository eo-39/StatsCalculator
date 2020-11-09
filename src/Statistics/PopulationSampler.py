from turtle import st

from src.Statistics.Statistics import Statistics


def __init__(self):
        self.stats = Statistics()
        pass

    # Simple random sampling
    def get_simple_random_sampling(self, size, seed, version, data):
        return self.get_rand_num_list_w_seed(size, seed, version, data)

    # Confidence Interval For a Sample
    def get_confidence_interval(self, data):

        conf_interval = st.t.interval(alpha=0.95
                        , df=len(data) - 1
                        , loc=self.stats.stats_mean(data)
                        , scale=st.sem(data)
                      )
        return conf_interval

        # Margin of Error
    def get_margin_of_error(self, data):
        margin_of_error = self.stats.divide(
                                self.stats.multiply(
                                        self.stats.stats_z_score(data)
                                            , (self.stats.stats_standard_deviation(data))
                                )
                                , self.stats.square_root(len(data))
        )
        return margin_of_error

    # Cochran’s Sample Size Formula
    def get_result_by_cochrans_sample_size(self, p1, p_diff, alpha, stats=None):
        if p_diff <= 0:
            raise ValueError("p_diff must be > 0")
        n = 1
        while True:
            z = self.stats.stats_z_score(p1, p1 + p_diff, n1=n, n2=n)
            p = 1 - stats.norm.cdf(z)
            if p < alpha:
                break
            n += 1
        return n

    # How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)
    def get_sample_size_by_confidence_interval_and_width(self, data):
        # step 1
        za_2 = self.stats.stats_z_score(self.stats.divide(self.get_confidence_interval(data)[0], 2))
        e = self.stats.divide(self.get_margin_of_error(self, data), 2)
        p = 0.5
        q = 1-p
        # step 2
        s2 = self.stats.multiply(p, q)
        # step 3
        s3 = self.stats.divide(za_2, e)
        # step 4
        s4 = self.stats.square(s3)
        # step 5 ( final )
        s5 = self.stats.multiply(s2, s4)
        # this is the sample population size for an unknown population standard deviation
        return s5

