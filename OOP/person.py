class Person:
    def __init__(self):
        self.name = "tony"
        self._secret = "hi"
        self.__msg = "This is private"
        self.__lol = "HAHAHA"


p = Person()

print(p.name)
print(p._secret)
# print(p.__msg) #error message
# print(dir(p))
print(p._Person__msg)
print(p._Person__lol)
