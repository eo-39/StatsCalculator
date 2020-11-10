from Statistics.StandardDev import stddev
from Statistics.Mean import mean


def zscore(a):
    zscorelist = []
    for k in a:
        zscorelist.append((k-(mean(a)))/(stddev(a)))
    return zscorelist