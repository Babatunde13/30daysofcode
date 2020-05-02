def unique(L):
    '''
    A function that takes  in a parameter L which is a list.
    Returns a list of unique numbers of the original list
    '''
    return f'Sample List: {L}\nUnique List: {sorted(list(set(L)))}'


print(unique([1,2,3,3,3,3,4,5]))
print(unique([1,2,3,3,3,3,4,5,3,3,3,3,4,5,6,6,11,22,33,44]))
print(unique([1,2,3,3,3,3,4,5,5,3,3,3,3,4,5,6,6,110,20,19,34]))
