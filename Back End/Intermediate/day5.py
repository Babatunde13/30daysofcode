def noSeven(number: int) -> list:
    '''
    A function that takes in an integer and removes all the occurences 
    of 7 by creating two variable such that the sum = number and there's no occurence of 7 in the list.

    Parameter: ----------------
            number: int
        
    Returns: a list of integers whose sum equal the parameter. and no occurence of 7 is in it.

    @author: Babatunde Koiki
    Created on: 05-04-2020
    '''
    a, b = '', ''
    for i in str(number):
        if i == '7':
            a += '5'
            b += '2'
        else:
            a+= i
            b += '0'
    return [int(a), int(b)]

print(noSeven(70))
print(noSeven(717))
print(noSeven.__doc__)
