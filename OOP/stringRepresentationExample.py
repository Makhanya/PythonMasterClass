"""
    String Representation Example
        The __repr__ method is one of several ways to provide a nicer string representation
"""


class Human:
    def __init__(self, name="somebody") -> None:
        self.name = name

    def __repr__(self) -> str:
        return self.name


dude = Human()
print(dude)
makhanya = Human(name="Makhanya Mzili")
print(f"{makhanya} is totally rad (probably)")

"""There are also several other dunders to return classes in string formats
(notably__str__ and __format__), and choosing one is ab bit complicated!"""
