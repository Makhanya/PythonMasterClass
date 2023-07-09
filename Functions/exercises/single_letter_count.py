'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''


def single_letter_count(word, letter):
    return word.lower().count(letter.lower())


print(single_letter_count("Hello World!", "l"))
print(single_letter_count("Hello World!", "h"))
print(single_letter_count("Hello World!", "z"))
