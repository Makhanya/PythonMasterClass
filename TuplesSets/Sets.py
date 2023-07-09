#   Sets
#       Sets are like formal mathematical sets
#       Sets do not have duplicate values
#       Elements in sets aren't ordered
#       You cannot access items in a set by index
#       Sets can be useful if you need to keep track of a collection of
#           elements, but don;t care about ordering, Keys or values and dulicate
#

# cities = ["Los Angeles", "Boulder", "Kyoto", "Florence", "Santiago",
#           "Los Angeles", "Shanghai", "Boulder", "San Francisco", "Oslo", "Tokyo"]

# print(len(set(cities)))

# print(set(cities))

#   Add
#       Adds an element to a set. If the element is already in the set, the set does'nt change
# s = set([1, 2, 3, 6, 7, 8])
# s.add(5)
# print(s)
# s.add(4)
# print(s)

#   Remove
#       removes a value from the set - returns a KeyError if the value is not found

# s.remove(3)
# print(s)

# #   Set Math
#       Sets have quite a few other mathematics methods
#           including
#               Intersection
#               symmetric_difference
#               union

# Suppose I teach two classes:
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

#   To generate a set with all unique students
print(math_students | biology_students)

#   To generate a set with students who are in both courses
print(math_students & biology_students)
