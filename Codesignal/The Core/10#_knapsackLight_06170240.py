def knapsackLight(v1, w1, v2, w2, maxW):
    if maxW >= w1 + w2:
        return v1 + v2
    elif v1 > v2 and maxW >= w1:
        return v1
    elif v2 > v1 and maxW >= w2:
        return v2
    elif v1 > v2 and maxW <= w1 and maxW >=w2:
        return v2
    elif v2 > v1 and maxW <= w2 and maxW >=w1:
        return v1
    elif v1 == v2:
        return v1
    else:
        return 0
