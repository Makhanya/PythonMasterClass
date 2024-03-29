class Aquatic:
    def __init__(self, name):
        print("Aquatic init")
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"


class Ambulatory:
    def __init__(self, name):
        print("Ambulatory init")
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land!"


class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        print("Penguin init")
        super().__init__(name=name)


# jaws = Aquatic("Jaws")
# # print(jaws)
# lassie = Ambulatory("Lassie")
# print(lassie)
captain_cook = Penguin("Captain Cook")
# print(captain_cook.swim())
# print(captain_cook.walk())
# print(captain_cook.greet())
#
# print(f"captain_cook is instance of Penguin: {isinstance(captain_cook, Penguin)}")
# print(f"captain_cook is instance of Aquatic: {isinstance(captain_cook, Aquatic)}")
# print(f"captain_cook is instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}")