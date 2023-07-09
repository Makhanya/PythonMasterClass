"""
    doctest
        *We can write test for functions inside of the docstring
        *Write code that looks like its inside of a REPL

        doctest Example
        def add(x, y):
  add together x and y
>> > add(1, 2)
 3

  >> > add(8, "hi")
   Traceback(most recent call last):
        ....
    TypeError: unsorported operand type(s) for +: 'int' and 'str'
    """


def add(a, b):
    """
    >>> add(2,3)
    6
    >>> add(100,10)
    1000
    """
    return a*b
"""

    Issues withd docktests
        *Sysntax is a little strange
        *Clutters up our function code
        *Lacks many features of larger testing tools
        *Tests can be brittle
"""