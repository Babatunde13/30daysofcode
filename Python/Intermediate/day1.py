
def average(numbers: str) -> int:
    '''
    A function that takes in different numbers in a single string and returns the average of the numbers

    Parameters: -------------
                numbers: str, a text containing numbers seperated by space.

    Returns: --------------
                an integer, avearge value of the numbers.

    @author: Babatunde Koiki
    Created on: 01-05-2020
    '''
    
    numbers = [int(number) for number in numbers.split()]
    return sum(numbers)/len(numbers)

print(average('12 11 2 6 7 10'))
