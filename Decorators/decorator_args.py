def shout(fn):
    def wrapper(name):
        return fn(name).upper()

    return wrapper


@shout
def greet(name):
    return f"Hi, I'm {name}"


@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please"


print(greet("todd"))
"""
    Decorator Pattern
"""


def my_decorator(fn):
    def wrapper(*args, **kwargs):
        # do some stuff with fn(*args, **kwargs)
        pass

    return wrapper
