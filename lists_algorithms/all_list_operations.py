from collections import deque
from functools import reduce

# addCreating and Initializing a List
def create_list(elements=None):
    return elements if elements is not None else []

# Adding Elements
def append_element(lst, element):
    lst.append(element)
    return lst
# insert elements to a list

if __name__ == "__main__":
    
    lst = create_list([1, 2, 5, 6])
    append_element(lst, 3)
    
