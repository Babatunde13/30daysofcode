def Atongue(string: str) -> str:
    '''
    A function that encrypts a text in a particular order
    It shifts the following word by index of 3 'aiyeou', and this by index of 10 'bkxznhdcwgpvjqtsrlmf'.

    Parameter: string, str. Text to decrypt

    Returns: The decrypted text

    @author: Babatunde Koiki
    Created on: 06-05-2020
    '''
    vowel = 'aiyeou'
    consonant = 'bkxznhdcwgpvjqtsrlmf'
    new_string = ''
    for char in string:
        if char.lower() in vowel:
            x = vowel.index(char.lower())
            if x+3 < len(vowel):
                if char.islower(): new_string += vowel[x+3]
                else: new_string += vowel[x+3].upper()
            else:
                if char.islower(): new_string += vowel[x+3-len(vowel)]
                else: new_string += vowel[x+3 - len(vowel)].upper()
        elif char.lower() in consonant:
            x = consonant.index(char.lower())
            if x+10 < len(consonant):
                if char.islower(): new_string += consonant[x+10]
                else: new_string += consonant[x+10].upper()
            else:
                if char.islower(): new_string += consonant[x+10-len(consonant)]
                else:  new_string += consonant[x+10-len(consonant)].upper()
        else: new_string += char
    return new_string
print(Atongue('As a boss, I refuse to speak the tongue of Mortal Men') == 'Eh e pihh, O dagyha ni hbaev nsa nitfya ig Widnec Wat')
