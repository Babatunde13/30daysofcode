def Triangle_no(num: int) -> bool:
    '''
    A function named Triangle_no that checks if a number is a triangle number
        A number is referred to as a triange number if the product of 8 and  the number sum to 1 is a perfect square.

        Parameter: --------------
                num:, int. The number to determine if it's a triangle number

    Returns: bool, True if num is triangular, Flase if otherwise.
    '''
    assert type(num) == int and num >0
    return not (8*num+1)**0.5 % 1 > 0

def error(func, num):
    try:
        return func(num)
    except AssertionError: return 1
Triangle_no(12)==False # 2 points
error(Triangle_no, -4)== 1# 2 points
error(Triangle_no, 'a')== 1 # 2 points
Triangle_no(1234)==False # 2 points
Triangle_no(-11)==1 # 2 points
Triangle_no.__doc__ != None # 2 points
Triangle_no(6)==True