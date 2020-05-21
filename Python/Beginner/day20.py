def create_array(rowNum: int , colNum: int) -> list:
    '''
    A function that generates a square matrix where each element is the product of it's row and column number.

    Parameters: rowNum: int, number of rows in the array
                colNum: int, number of columns in the array.
    
    Returns: an array
    @author: Babatunde Koiki
    Created on 20-05-2020
    '''
    assert type(rowNum)==type(colNum)==int and rowNum > 0 and colNum > 0, 'Invalid input'
    return [[row*col for col in range(colNum)] for row in range(rowNum)]


print(create_array(3, 5))
print(create_array(-1, 1))