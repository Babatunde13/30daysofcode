def is_perfect_square(number: int) -> bool:
    '''
    A function that takes in a parameter number and checks if it is a prime number
    
    Parameter: ----------
              number: integer, number to be checked if it is a [erfect square or not.
              
    Returns:True if perfect square and False not. 
    
    @author: Sodiq Agunbiade
    '''
    for i in range(number//2):
        if i * i == number:
            return True
    return False

