"""
    Polymorphism
        A key principle in OOP is the idea of polymorphism- an object can take on many(poly) form(morph)

        While a formal definition of polymorphism is more difficult, here are two important practical applications:

        1.The same class method works in a similar way for different classes
            Cat.speak() #meow
            Dog.speak() #woof
            Human.speak() #yo
        2.The same operation works for different kinds of objects
            sample_list = [1,2,3,4]
            sample_tuple = (1,2,3,4)
            sample_string ="awesome"

            len(sample_list)
            len(sample_tuple)
            len(sample_string)

    Polymorphism & Inheritance
        1.The same class method works iin a similar way for different classes
            A common implemenation of this is to have a method in a base (or parent)
            class that is overridden by a subclass. This is called method overloading
                Each subclass will have a different implemetation of the method.
            class Animal():
                def speak(self):
                    raise NotImplementedError("Subclass needs to implement this method")
            class Dog(animal):
                def speak:
                    return "woof"
            class Cat(Animal):
                def speak(self):
                    return "meow"


"""