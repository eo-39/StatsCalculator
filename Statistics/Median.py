def median(a):
    a.sort()
    mid = len(a) // 2
    return (a[mid] + a[~mid]) / 2