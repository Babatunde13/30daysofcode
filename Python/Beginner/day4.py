def string_test(s):
    '''
    A function string_test that takes a parameter 's' which is a string and counts the number of 
    Upper and lowercase letters in the string.
    Returns: The count of the upper and lower case letters 
    '''
    u, l = (0, 0)
    for i in s:
        if i.isupper(): u += 1
        if i.islower(): l += 1
    return f'Number of Lowercase letters is {l}.\nNumber of Uppercase letters is {u}.'


