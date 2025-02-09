# function with on parameter
def function_with_one_param(name: str,) -> str:
    return f"Hello,{name}! thanks for coming by"

username = input("Enter your name: ")
output = function_with_one_param(username) 
print(output)
