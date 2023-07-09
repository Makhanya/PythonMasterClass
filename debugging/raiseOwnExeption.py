""" 
    Raise your Own Exceptions
    
        in python we can also throw errors using the raise keyword
        This sis helpful whe creating your own kinds of exception and error messages
        
        #raise ValueError('invalid value')"""

# for x in range(0, 11):
#     if x == 6:
#         raise ValueError("invalid value")
#     print(f"The value is {x}")


def colorize(text, colour):
    colours = ("cray", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("Text must be instance of str")
    if colour not in colours:
        raise ValueError("colour is invalid colour")
    print(f'Printed {text} in {colour}')


print("hi")
colorize("hi", "red")
colorize(43, "red")
