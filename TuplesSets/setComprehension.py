#   Set Comprehension
print({x**2 for x in range(10)})


def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'}) == 5
