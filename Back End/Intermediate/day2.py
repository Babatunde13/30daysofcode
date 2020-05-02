def myFunction(num: int) -> int:
    '''
    Function that checks the number of times the number in num until it turns to a single number

    Parameter: ------------- 
                num: int, must be greater than 0
    
    Returns: ------------
                count: int, the number of times *num* can multiply the numbers in it to become a single number.
    
    @author: Babatunde Koiki
    Created on: 02-05-2020
    '''
   
    assert num > 0, 'Number must be positive'
    count = 0
    while len(str(num)) > 1:
        i = 1
        for j in str(num):
            i = i * int(j)
        num = i
        count += 1
    return count

print(myFunction(43)) # 2
print(myFunction(23413)) # 3
print(myFunction(0)) # 0
print(myFunction(-12)) # AssertionError: Number must be positive
