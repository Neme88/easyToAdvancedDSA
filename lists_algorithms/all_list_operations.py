from collections import deque
from functools import reduce

# addCreating and Initializing a List
def create_list(elements=None):
    return elements if elements is not None else []

# 3 methods of Adding Elements to a list  
# 1 append to the end of the list
def append_element(lst, element):
    lst.append(element)
    return lst
# 2 insert elements to any given index of a list
def insert_element(lst, index, element):
    lst.insert(index, element)
    return lst
# 3 extend method to add multiple elements
def extend_list (lst, new_element):
    lst.extend(new_element)
    return lst
# remove element from a list


if __name__ == "__main__":
    
    lst = create_list([1, 2, 5, 6])
    res0 = append_element(lst, 3)
    res1 = insert_element(lst, 1, 99)
    res2 = extend_list(lst, [1, 2, 5, 6 ])
    print(res0)
    print(res1)
    print(res2)
    
    
    
