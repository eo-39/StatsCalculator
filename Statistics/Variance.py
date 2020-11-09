def get_variance(data):
    x1 = get_mean(data)
    num_values = len(data)
    total = 0
    total1 = 0
    data1 = []
    for i in data[0:]:
        a = data[i - 1]
        total = (a - x1) ** 2
        data1.append(total)
    total1 = sum(data1)
    return division(num_values - 1, total1)
