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
    
    return math.prod(args)


prod = variableLengthFunctiontwo(2,6, 3) 
print(prod)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "one":
            variableLengthFunctionOne()
        elif sys.argv[1] == "two":
            variableLengthFunctiontwo()
        else:
            print("Invalid argument. use one or two.")
            
    