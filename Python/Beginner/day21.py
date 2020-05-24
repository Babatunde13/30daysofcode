def var_sort(*data) -> list:
    '''
    A function named var_sort that takes in an arbitrary number of tuples and sorts it in ascending order
    
    Parameter: *data: tuple of tuple
    
    Returns: list of tuple

    Created on: 21-05-2020
    @author: Babatunde Koiki
    '''
    assert all([type(d)==tuple for d in data]), 'Input must  be a tuple'
    assert all([len(d)==3 for d in data]), 'Each element must contain 3 values.'
    assert all([type(d[0])==str and type(d[1])==type(d[2])==int and d[1]>0 and d[2]>0 for d in data]), 'First element in each argument must be a string while the remaining two elements must be a positive integer'
    return sorted([d for d in data], key= lambda x: (x[0], x[1], x[2]))


def error(func, *args):
    try:
        return func(*args)
    except AssertionError:
        return 1

error(var_sort, ('Jane', 11, 2),  ('Bame', 12, 34), (('Tom', 12, 22)))==[('Bame', 12, 34), ('Jane', 11, 2), ('Tom', 12, 22)] # 2 points
error(var_sort, (1, 1, 1))==1 # 2 points
error(var_sort, ('ade', 11, 2), ('ade', 10, 12), ('ade', 11, 3))==[('ade', 10, 12), ('ade', 11, 2), ('ade', 11, 3)] # 2 points
error(var_sort, ('ade', 2), ('ade', 3, 5)) == 1  # 2 points
error(var_sort, ('ade', 12, 11), ('John', -1, 2))==1 # 2 points
error(var_sort, ('old', 10, 12), ('Old', 10, 12), ('name', 17, 20))==[('Old', 10, 12), ('name', 17, 20), ('old', 10, 12)] # 2 points
error(var_sort, 1) == 1 # 2 points

