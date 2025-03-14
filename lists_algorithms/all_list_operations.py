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
# insert elements to any given index of a list
def insert_element(lst, index, element):
    lst.insert(index, element)
    return lst

# 

if __name__ == "__main__":
    
    lst = create_list([1, 2, 5, 6])
    append_element(lst, 3)
    res = insert_element(lst, 1, 99)
    print(res)
    
    
    
