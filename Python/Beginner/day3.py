def is_even(num):
    '''
    A function that checks if a given number is even.
    Returns True if the number is even and false if otherwise.
    '''
    if num % 2 == 0:
        return True
    return False

def even_odd(list_num):
    '''
    A function that uses the function is_even to filter all the even numbers 
    in a list and also gets the number of odd numbers in the list and also the finds the number of even numbers in the
    list and prints them out 
    
    Returns the number of even and odd numbers in the list.
    '''
    even = [i for i in list_num if is_even(i)]
    return(f'number of even numbers is {len(even)}\nnumber of odd numbers is {len(list_num) - len(even)}')

print(even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18]))
print(even_odd(range(10, 35)))
