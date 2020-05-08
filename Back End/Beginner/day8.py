def count(num: int) -> int:
    '''
    A function that converts a number to binary and returns the number of 1s present.
    Parameter: num
    @author: Babatunde Koiki
    Created on: 08-05-2020
    '''
    return "Invalid, number can't be negative" if num < 0 else int(bin(num)[2:].count('1'))
