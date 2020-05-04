def Cstrings(text: str) -> str:
    '''
    A function that returns a word converted to uppercase and lowercase.

    Parameter: -------------
                text, str. The text with both upper case and lower case that we want to convert to upper and lower case.

    Return: -----------
                The text in upper and lower case.

    @author: Babatunde Koiki
    Created on: 04-05-2020
    '''
    return f'{text.upper()}, {text.lower()}'

print(Cstrings("HasTaLAvisTA")) # HASTALAVISTA, hastalavista
