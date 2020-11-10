from collections import Counter


def mode(a):
    datalist = Counter(a)
    return [k for k, v in datalist.items() if v == datalist.most_common()]