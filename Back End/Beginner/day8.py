def count(num: int) -> int:
    '''
    A function that converts a number to binary and returns the number of 1s present.
    @author: Babatunde Koiki
    Created on: 08-05-2020
    '''
    return int(bin(num)[2:].count('1'))
