li = [[1, 2, 3, 4], [3, 4, 5, 6], [4, 3, 2, 6, 7, 8]]
# print(len(li))
print(li[2][-1])

#   printing values in Nested List

for l in li:
    for val in l:
        print(val)

coords = [[10.423, 9.132], [37.212, -14.092], [21.367, 32.572]]

for loc in coords:
    print(loc)

print()
for loc in coords:
    for coord in loc:
        print(coord)
