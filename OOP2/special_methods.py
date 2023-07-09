from copy import copy


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="NewBorn", last=self.last, age=0)
        return "You can't add that"

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return TypeError("Cant multiply")


j = Human("Jenny", "Larson", 47)
k = Human("Khanya", "Mzili", 30)
# print(j)
# print(k)
# print(j + k)
# print(k *'a')

triplets = j * 3
triplets[1].first = "Jessica"
print(triplets)
# khanya and jenny having triplets
triplets =(k + j) * 3
print(triplets)