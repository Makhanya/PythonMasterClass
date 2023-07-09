"""
    Class methods
        class methods are methods(with the @classmethod decorator)
            that are not concerned with the instances, but the class itself
            
class Person():
    # .....
    @classmethod
    def from_csv(cls, filename):
        return cls(*params)  # This is the same as calling Person(*params)


Person.from_csv(my_csv)

"""



