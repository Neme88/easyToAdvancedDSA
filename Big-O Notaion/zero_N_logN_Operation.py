# the following code implements the the merge sort algorithm as an O(n* log n) time complexity

def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    
    # Divide 
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Conquer or Merge
    return merge(left_half, right_half)
def merge(left_half: list, right_half: list) -> list:
    result = []
    i = 0
    j = 0
    
    # merge the two half arrays
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
    
    
