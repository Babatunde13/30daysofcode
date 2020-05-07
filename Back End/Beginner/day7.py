def Psum(list1: list, list2: list) -> int:
    '''
    A function that takes two lists of same lenght, multiplies the element with same index.
    
    Parameters: ---------
                list1: list 
                list2: list

    Returns: The sum of element-wise product of two lists

     @author: Babatunde Koiki
    Created on: 07-05-2020
    '''
    assert type(list1)==type(list2)==int and all(isinstance(x, int) for x in list1) and all(isinstance(x, int) for x in list2), 'Invalid input'
    return sum(map(lambda x, y: x*y, list1, list2))

print(Psum([2, 6, 9, 4], [1, 2, 4, 8]))
print(Psum([1, 2, 'q'], [3, 'b', 1]))