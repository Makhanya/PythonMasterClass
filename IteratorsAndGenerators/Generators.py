"""
    Generators
        *Generators are iterators
        *Generators can be created with generator functions
        *Generator functions use the yield keyword
        *Generators can be created with generator expressions

        Functions vs Generator Functions
           *Functions
                -Uses return
                -return once
                -When invoked, returns the return value
           *Generator Functions
                -uses yield
                -can yield multiple times
                -When invoked, return a generator
                    Our first Generator
                        def count_up_to(max):
                            count =1
                            while count<= max:
                                yield count
                                count +=1

        Generator Expressions
            *You can also create generators from generator expressions
            *Generator expressions look a lot like list complrehensions
            *Generator expressions use() instead of []
"""