def squareSum(n):
    if type(n)!=int: return 'Invalid!'
    if n < 0: return 'Wrong Input'
    
    return sum(range(n))**2 - sum([x**2 for x in range(n)])

squareSum(10)==1740 # 3 points
squareSum(-1)=='Wrong Input' # 2 points
squareSum('a')=='Invalid!' # 2 ppoints
squareSum(100)==24174150 # 3 points
squareSum.__doc__ != None # 1 point
squareSum(123))==55682264# 3 oints