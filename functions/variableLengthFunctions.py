import sys
import math
# implement function with Variable argument length
def variableLengthFunctionOne(*args):
    
    # check for Negative number 
    if any(arg < 0 for arg in args):
        return "Negative number argument not allowed"
   
    # check for empty argument list
    if not args:
        return 2
    # check for single argument list
    if len(args) == 1:
        return args[0]

    else:
        return sum(args)

res = variableLengthFunctionOne(12)

print(res)


def variableLengthFunctiontwo(*args):
    
    # check for Negative number 
    if any(arg < 0 for arg in args):
        return "Negative number argument not allowed"
    
    # check for empty argument list
    if not args:
        return "We need at least one argument"
    
    # check for single argument list
    if len(args) == 1:
        return args[0]
    
    else:
        return math.prod(args)


prod = variableLengthFunctiontwo(23, 2, 4) 
print(prod)


def variableLengthFunctionThree(*args: int) -> int:
        # compare string length
        max_len = max(len(str(arg)) for arg in args)
        return max_len
    
max_string = variableLengthFunctionThree("long", "longer")
print(max_string)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "one":
            variableLengthFunctionOne()
        
        elif sys.argv[1] == "two":
            variableLengthFunctiontwo()
        
        elif sys.argv[1] == "three":
            variableLengthFunctionThree()
        else:
            print("Invalid argument. use one or two.")
            
    