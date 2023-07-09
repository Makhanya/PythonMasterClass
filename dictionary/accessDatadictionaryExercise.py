# artist = {
#     "first": "Neil",
#     "last": "Young"
# }
# #   Accessing Individual Values
# #       instructor["name"]
# # print(artist)

# full_name = artist["first"] + " " + artist["last"]
# print(full_name)

# #   How to iterate of a dictionary
#       Accessing All values in a dictionary

# Use.values()

# for value in artist.values():
#     print(value)

#   Accessing All Keys and values
#    Use.items()

# for key,value in instructor.items():
#        print(key,value)

instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}
for key, value in instructor.items():
    print(f"{key} : {value}")
