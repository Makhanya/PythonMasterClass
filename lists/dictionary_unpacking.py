""" Using ** as an Argument: Dictionary Unpacking"""


def display_names(first, second):
    print(f"{first} says hello to {second}")


names = {"first": "Makhanya", "second": "Mzili"}

# display_names(names)  # nope..
#display_names(first="Sino", second="Hlumela")
# display_names(**names)  # Makhanya says hello to Mzili


def add_and_multiply_numbers(a, b, c, **kwargs):
    print(a+b*c)
    print("Other Stuff...")
    print(kwargs)


data = dict(a=1, b=2, c=3, d=55, name="tony")

# add_and_multiply_numbers(data)  # TypeError
add_and_multiply_numbers(**data, cat="blue")
