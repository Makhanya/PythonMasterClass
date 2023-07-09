

# answer = [friend[0] for friend in ['Elie', 'Tim', 'Matt']]
# print(answer)

# answer2 = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
# print(answer2)

# answer = [num for num in [1, 2, 3, 4] if num in [3, 4, 5, 6]]
# print(answer)

# answer2 = ["".join(reversed(value.lower()))
#            for value in ['Elie', 'Tim', 'Matt']]  # [val[::-1].lower() for val in ["Elie","Tim", "Matt"]]
# print(answer2)

# answer = ([x for x in range(1, 101) if x % 12 == 0])
# print(answer)

# exercise 4
answer = [''.join(val)
          for val in "amazing" if not val in ('a', 'e', 'i', 'o', 'u')]  # answer = [char for char in "amazing" if char not in "aeiou"]

print(answer)
