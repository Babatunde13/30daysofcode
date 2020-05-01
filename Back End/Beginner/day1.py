def factor(num: int) -> tuple:
    '''
    A function named factor which uses binary search to reduce the complexity of the algorithm, .

    Parameter: -------
                num: Integer, the number we want to get it's factors

    Returns: ---------
                a tuple of integers, where each integers are the factors of the number excluding the numbers itself.

    @author: Babatunde Koiki
    Created on: 01-05-2020
    '''
    return tuple([i for i in range(1, num//2 + 1) if num % i == 0])

print(factor(10)) # (1, 2, 5)
