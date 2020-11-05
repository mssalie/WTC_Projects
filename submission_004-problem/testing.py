
def find_min(element):
    """TODO: complete for Step 1"""

    for i in element:
        if isinstance(i, int) == False:
            return -1
    if len(element) <= 0:
            return -1
    elif len(element) == 1:
            return 1
    elif element[0] > element[1]:
        element[0] = element[1]
        element.remove(element[1])
        find_min(element)
        return element[0]
    else:
        element.remove(element[1])
        find_min(element)
    return element[0]

element = [-1,-2,-3,-5,-6]
print(find_min(element))


# def sum_all(element):
#     """TODO: complete for Step 2"""
#     for i in element:
#         if isinstance(i, int) == False:
#             return -1
#     if len(element) <= 0:
#         return - 1
#     elif len(element) == 1:
#         return element[0]
#     else:
#         element[0] = element[1]
#         element.remove(element[1])
#         sum_all(element)
#         return element[0]

# element = [1,2,4,5,6]
# print(sum_all(element))

# def find_possible_strings(character_set, n):
#     """TODO: complete for Step 3"""
    
#     prefix = []
#     for i in character_set:
#         if isinstance(i, int):
#             return prefix
    
#     if n == 1:
#         return character_set
    
#     for i in character_set:
#         for j in find_possible_strings(character_set, n -1 ):
#             prefix.append(i + j)
#     return prefix

# prefix = ["a","b"]
# print("\n".join(find_possible_strings(prefix, 3)))