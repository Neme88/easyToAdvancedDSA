# Searching & Counting list element
def find_index(lst, element):
    return lst.index(element) if element in lst else -1

# use case
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element_to_find = 5

index = find_index(my_list, element_to_find)
print(f'The index of {element_to_find} in the list is: {index}')