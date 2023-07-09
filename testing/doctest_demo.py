
# def add(x, y):
#     """
#         >>> add(2,3)
#         6
#         >>> add(4,5)
#         9

#     """
#     return x+y


def double(values):
    """ double the values in a list

    >>> double([1,2,3,4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> double([True,None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * element for element in values]
