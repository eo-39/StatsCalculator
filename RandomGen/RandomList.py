from RandomGen.RandomRange import randDec
from RandomGen.RandomRange import randInt


def randIntList(n, a, b):
    datalist = []
    for k in range(n):
        datalist.append(randInt(a, b))
    return datalist


def randDecList(n, a, b):
    datalist = []
    for k in range(n):
        datalist.append(randDec(a, b))
    return datalist