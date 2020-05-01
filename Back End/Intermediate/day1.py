
def scrabble(str1: str, str2: str) -> bool:
    '''
    A function that checks if it's first parameter has all the characters in the second parameter

    Parameters: -----------
                str1: str, A text
                str2: str, A text

    Returns: -----------
            Returns bool. True if condition is met, otherwise False. 

    @author: Babatunde Koiki

    Created on: 01-05-2020
    '''
    for i in str2:
        if i not in str1:
            return False
    return True

print(scrabble('jigokuhen','jigen'))
print(scrabble('i am rain', 'raining'))

