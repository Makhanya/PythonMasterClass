nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[[print(val) for val in l] for l in nested_list]


print([["X" if num % 2 != 0 else "O" for num in range(1, 4)]
      for val in range(1, 4)])
