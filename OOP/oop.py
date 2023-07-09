"""
    Objects
        *define what Object Oriented Programming is
        *Understand encapsulation and abstraction
        *Create classes and instances and attach
            methods and properties to each
    What is OOP?
        Object oriented programming is a method of programming
        that attempts to model some process or thing in the world as a class or object
        Class
            -a blueprint for objects.classes can contain 
                methonds(functions) and attributes(similar 
                to key in a dict).
        instance
            -objects that are constructed from a class blueprint
                that contain their class's methods and properties

    Why OOP?
        With object oriented programming, the goal is to encapsulate your code
        into Logical, Hierarchical grouping using classes so that you can reason about your 
        code at a higher level

        Example
            Say we want to model a game of poker in our program.
            We could have the following entities:
                Game
                Player
                Card
                Deck
                Hand
                Chip
                Bet
    Encapsulation
        Encapsulation - the grouping of public and private attributes 
        and methods into a programmatic class, making abstraction possible
        Example 
            Designing the Deck class, I make cards a private attribute (a list)
            I decide that the lenght of the cards should be accessed via a public method called count() --i.e deck.count()

    Abstraction
        Abstraction - exposing only "Relevent" data in a class interface, hiding
        private attributes and methods (aka the "inner working") from user

    Creating a Class
        class Vehicle:
            def __init__(self, make,model,year):
                self.make=make
                self.model=model
                self.year=year
            Classes in Python can have a special __init__ method, which gets
            called every time you create an instance of the class (instantiate).

    Instantiating a Class
        Creating an object that is an instance of a class is called instantiating a class
        v = Vehicle("Honda", "civic", 2007)

    Class Attributes
        We can also define attributes directly on a class that are shared by
            all instances of a class and the class itself
"""
