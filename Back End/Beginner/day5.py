def Triangle_no(num: int) -> bool:
    '''
    A function named Triangle_no that checks if a number is a triangle number
        A number is referred to as a triange number if the product of 8 and  the number sum to 1 is a perfect square.

        Parameter: --------------
                num:, int. The number to determine if it's a triangle number

    Returns: bool, True if num is triangular, Flase if otherwise.
    '''

    return not (8*num+1)**0.5 % 1 > 0

print(Triangle_no(6))
print(Triangle_no(10))
print(Triangle_no(8))
print(Triangle_no.__doc__)