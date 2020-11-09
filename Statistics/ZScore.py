def get_z_score(data):
    value_mean = get_mean(data)
    z = []
    for i in range(0, len(data)):
        a = subtraction(value_mean, data[i])
        b = division_float(get_standard_deviation(data), a)
        z.append(b)
    return z
