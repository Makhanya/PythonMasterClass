"""
    Objectives
        *Define what a module is
        *Import code from built-in modules
        *Import code from other files
        *Import code from external modules using pip
        *Describe common module pattenrns
        *Describe the request/response cycle in HTTP
        *Use the request module to make requests to web apps
        
    Why use Modules?
        *keep python files small
        *Reuse code across multiple files by importing
        *A module is just a Python file!

    Built-in Modules Example
        *import random
            print(random.choice(["apple", "banana", "cherry", "durian"]))
            print(random.shuffle(["apple", "banana", "cherry", "durian"]))

            import random as omg_so_random
                omg_so_random.choice

    Importing Parts of a Module
        *The from keyword lets you import parts of a module
        *Handy rule ot thumb: only import what you need!
        *If you still want to import everything, you can also use
            the From Module import * pattern

    Different ways to import
        All of these work
            *import random
            *import random as omg_so_random
            *from random import *
            *from random import choice, shuffle
            *from random import choice as gimme_one, suffle as mix_up_fruits
"""


from random import choice, randint, shuffle
print(choice(["apple", "banana", "cherry", "durian"]))
print(shuffle(["apple", "banana", "cherry", "durian"]))
print(randint(1, 100))
