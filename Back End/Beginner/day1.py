def factor(num):
    return tuple([i for i in range(1, num) if num % i == 0])

print(factor(10))
