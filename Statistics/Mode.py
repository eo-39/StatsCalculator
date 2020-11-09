def get_mode(data):
    data1 = data
    maximum = data1.count(data1[0])
    m = data1[0]
    for i in range(1, len(data1)):
        freq = data1.count(data1[i])

        if freq > maximum:
            maximum = freq
            m = data1[i]
        else:
            pass
    return m
