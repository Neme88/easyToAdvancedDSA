def average(table=[]):

    if not table: #O(1)
        return 0
    if not isinstance(table, list): #O(1)
        return str("Input must be list")
    if len(table) == 1: #O(1)
        return table[0]
    if not all(isinstance( item, (int, float)) for item in table): #O(n)
        return "table must be numbers"
    return sum(table) / len(table) #O(n)

# Big-O complexity is O(2n) which ends of becoming O(n) due to the constant dropping rules.

# planned optimization for this algorithm includes 
# Preprocessing input.
# Lazy validation.
# Precomputing and caching sums.
# Using a running sum and count for dynamic datasets.

input_One = [2,3,4,79,34,67, 12, 100, 10, 12,]
input_Two = ['2','4','5',6]
input_three = 78
input_four = [3]
input_five = []
table_one = average(input_Two)
print(table_one)