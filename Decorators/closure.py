from random import choice


# Inner functions can access outer function scope
def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(("Hahaha", "Lol", "tehehe"))
        return f"{laugh} {person}"

    return get_laugh


laugh_at = make_laugh_at_func("linda")

print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
