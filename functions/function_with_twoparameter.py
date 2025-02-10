# a function with two parameters
def function_with_two_params(param1: int, param2: int) -> int:
    if param1  <= 0 or param2  <= 0:
        return ("Both parameters should be greater than zero")
    else:
        return param1 + param2
# testing the function
res = function_with_two_params(0, 4)

print(res)
