"""

Special Methods
        2.(Polymorphism) The same operation works for different kinds of objects
            How does the following work in Python
                8 + 2 #10
                "8" + "2" #82

                The answer is "special method"
                Python classes have special(also known as "magic") methods, that are
                dunders(i.e double underscore-named).

                There are methods with special names that give instructions to python for how to deal with objects
        Special Methods Example
            What is happening in our example?
                8 + 2 #10
                "8" + "2" #82

                The operator is shorthand for a special method called __add__() that gets called on the first operand
                If the first(left_ operand is an instance of int, __add__() does mathematical addition. If it's a string,
                it does string concatenation
        Special Methods Applied
            Therefore, you can declare special methods on your own classes to mimic
                the behavior of builtin objects, like so using __len__
            class Human:
                def __init__(self, height):
                    self.height = height #in inches
                def __len__(self):
                    return self.height
            mk=Human(60)
            lan(mk) #60
        String Representation
            The most common use-case for special methods is to make classes "look pretty" in strings
            By default, our classes look ugly:
            class Human:
                pass
            mk = Human()
            print(mk) #<__main__.Human at 0x1062b8309>
        String Representation Example
            The __repr__ method is one of several ways to provide a nicer string representation
            class Human:
                def __init__(self, name="somebody"):
                    self.name = name
                def __repr__(self):
                    return self.name
            dude = Human()
            print(dude) #"somebody"


"""