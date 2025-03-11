from collections import deque
from functools import reduce

# addCreating and Initializing a List
def create_list(elements=None):
    return elements if elements is not None else []

# use case
my_list = create_list([1, 2, 3, 4, 5])
print(f'Original List: {my_list}')

# Adding Elements
def append_element(lst, element):
    lst.append(element)
    return lst


# use case
my_list = append_element(my_list, 6)
print(f'List after adding element: {my_list}')

if __name__ == "__main__":
    lst = create_list([1, 2, 5, 6])
    append_element(lst, 3)
    
