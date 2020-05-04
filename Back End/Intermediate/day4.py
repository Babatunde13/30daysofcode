def isPrime(num: int) -> bool:
    '''
    A function that checks if a number is prime.

    Parameters: -----------
                num: int, Number to check if is prime.

    Return: ------------
            bool: True if number is prime, otherwise False.
        
    @author: Babatunde Koiki
    Created on: 04-05-2020
    '''
        for i in range(2, int(num * 0.5)+1):
            if num % i == 0: return False
        return True

def OptimusPrime(num: int) -> list:
    '''
    A function that returns a list containing all the prime numbers between 1 and num inclusive.

    Parameters: ------------
                num, int. Number to end the list.

    Returns: ----------
            a list of all prime numbers between 1 and num.

    @author: Babatunde Koiki
    Created on: 04-05-2020
    '''
    return [i for i in range(2, num+1) if isPrime(i)]

print(OptimusPrime(7))

        
