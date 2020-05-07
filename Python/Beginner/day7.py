def averageMultiple(n):
    return [i for i in range(1, n) if i % 3 == 0  or i % 5 == 0]
    return sum(x)/len(x)

averageMultiple(10)