# the following code implements the the merge sort algorithm as an O(n* log n) time complexity

def merger_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    
    
