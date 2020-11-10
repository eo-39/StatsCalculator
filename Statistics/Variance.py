from Statistics.Mean import mean


def variance(a):
    avg = mean(a)

    return sum((k - avg) ** 2 for k in a) / len(a)