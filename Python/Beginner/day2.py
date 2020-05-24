def missing_numbers(num_list):
    '''
    A function that takes in a parameter num_list and checks for the missing numbers in the list
    according to preference.
    
    Returns:
          a sorted list of the missing values of num_list
    '''






    original_list = [x for x in range(min(num_list), max(num_list))]
    return sorted(list(set(original_list)-set(num_list)))

