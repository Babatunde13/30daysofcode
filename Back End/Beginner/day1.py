def myFunction(num: int) -> int:
    '''
    A function named factor which uses binary search to reduce the complexity of the algorithm, .

    Parameter: -------
                num: Integer, the number we want to get it's factors

    Returns: ---------
                The number of factors the number has excluding itself.

    @author: Babatunde Koiki
    Created on: 01-05-2020
    '''
    
    return len([i for i in range(1, num//2 + 1) if num % i == 0])

print(myFunction(10)) # 3
