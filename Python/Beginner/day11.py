def squareSum(n):
    if type(n)!=int: return 'Invalid!'
    if n < 0: return 'Wrong Input'
    
    return sum(range(n))**2 - sum([x**2 for x in range(n)])

