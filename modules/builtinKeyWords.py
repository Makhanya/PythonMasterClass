import keyword


def contains_keyword(*args):
    for x in args:
        if keyword.iskeyword(x):
            return True
    return False


print(contains_keyword("hello", "goodbye"))  # False

print(contains_keyword("def", "haha", "lol", "chicken", "alaska"))  # True

print(contains_keyword("four", "for", "if"))  # True

print(contains_keyword("blah", "doggo", "crab", "anchor"))  # False

print(contains_keyword("grizzly", "ignore", "return", "False"))  # True
