
def find_min(element):
    """TODO: complete for Step 1"""

    '''
    This function returns the smallest value in a list of numbers
    '''
    
    for i in element:
        if isinstance(i, int) == False:
            return -1
    
    if len(element) <= 0:
        return -1
    
    elif len(element) == 1:
        return element[0]
    
    elif element[0] > element[1]:
        element[0] = element[1]
        element.remove(element[1])
        find_min(element)
        return element[0]
    
    else:
        element.remove(element[1])
        find_min(element)
        return element[0]


def sum_all(element):
    """TODO: complete for Step 2"""

    '''
    This function returns the sum of all values in a list.
    '''

    for i in element:
        if isinstance(i, int) == False:
            return -1
    
    if len(element) <= 0:
        return - 1
    
    elif len(element) == 1:
        return element[0]
    
    else:
        element[0] += element[1]
        element.remove(element[1])
        sum_all(element)
        return element[0]


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    
    '''
    This function returns all possible permutations of strings in a list.
    '''

    prefix = []
    for i in character_set:
        if isinstance(i, int):
            return prefix
    
    if n == 1:
        return character_set
    
    for i in character_set:
        for j in find_possible_strings(character_set, n -1 ):
            prefix.append(i + j)
    return prefix
