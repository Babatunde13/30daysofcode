def k_largest(list_, n):
    # list(sorted(list_, reverse=True)).index([n-1]))
    return sorted(list_, reverse=True)[n-1]




k_largest([1, 4, 7, 2, 22, 34, 21, 44, 5, 3], 3)==22 # 3 points
k_largest([3, 555, 2, 11, 444, 12, 24, 42, 244], 5)==24 # 3 points
k_largest([121, 3232, 2323, 43, 2321, 4223, 24232, 222], 3)==3232 # 3 points
k_largest([12, 22, 123, 1, 4, 2, 5, 433, 45, 67], 4)==45 # 3 points
k_largest.__doc__ != None # 1 point
k_largest([1, 2, 3, 4, 5, 6], 1)==6 # 2 points