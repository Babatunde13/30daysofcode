def myFunction(text: str) -> bool:
    '''
    Function that checks if a text is palindrome.
    A palindrome text is one that is same as it's reversed text after removing the spaces.

    Parameter: ------------- 
                text: str, word(s) to check if it's palindrome
    
    Returns: ------------
                True if palindrome, False if otherwise.
    
    @author: Babatunde Koiki
    Created on: 02-05-2020
    '''
    if text.replace(' ', '') == text.replace(' ', '')[::-1]:
        return True
    return False

print(myFunction('Howdy')) # False
print(myFunction('madam')) # True
