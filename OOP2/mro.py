"""
    Method Resolution order (MRO)
        whenever you create a class, Python sets a Method Resolution Order, or
        MRO, for the class, which is the order in which Python will look for methods for instance of that class

        You can programmatically reference the MRO three ways:
            *__mro__ attribute on the class
            *use the mro() method on the class
            *use the builtin help(cls) method
    """


class A:
    def do_something(self):
        print("Method Defined In: A")


class B(A):
    def do_something(self): print("Method Defined In: B")


class C(A):
    def do_something(self): print("Method Defined in:C")


class D(B, C):
    pass
    # def do_something(self):
    #     print("Method Defined In: D")

# print(D.__mro__)
# print(D.mro())
# help(D)

# thing = D()
# thing.do_something()
