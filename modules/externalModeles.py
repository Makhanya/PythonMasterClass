""" 
    External Modules
        *Built-in modules come with Python
        *External modules are downloaded from the internet 
        *You can download external modules using pip
        
        pip
            *Package management system for python
            *As of 3.4 comes with Python by default
            *python3 -m pip install NAME_OF_PACKAGE """
# import sys
# from termcolor import colored, cprint

# text = colored('Hello, world!', 'red', attrs=['reverse', 'blick'])
# print(text)
# cprint('Hello, World!', 'green', 'on_red')


# def print_red_on_cyan(x): return cprint(x, 'red', 'on_cyan')


# print_red_on_cyan("Hello, World!")
# print_red_on_cyan("Hello, Universe!")

# for i in range(10):
#     cprint(i, 'magenta', end=' ')

# cprint("Attention!", "red", attrs=['bold'], file=sys.stderr)
from termcolor import colored

text = colored("Hi There!", color="magenta",
               on_color="on_green", attrs=["blink"])
print(text)
