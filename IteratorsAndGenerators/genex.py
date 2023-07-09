def num():
    for num in range(1, 10):
        yield num


g = num()
print(g)
# for x in range(10):
#     print(next(g))

gen = (num for num in range(1, 10))
print(gen)
# print(next(gen))
