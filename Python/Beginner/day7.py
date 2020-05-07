def averageMultiple(n):
    '''
    A function that returns the average of multiples of 3 or multiples of 5 from 1 to n without including n.

    Parameter: ----------
                n: int
    Returns: int, sum 

    @author: Babatunde Koiki
    Created on: 07-05-2020
    '''
    x = [i for i in range(1, n) if i % 3 == 0  or i % 5 == 0]
    return sum(x)/len(x)

averageMultiple(10)