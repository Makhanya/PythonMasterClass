data = [1, 2, 3, 4]
data.append("Color")
data.append("Makhanya")

print(data)
print("Extend")
data.extend(["Blue", "Bulls", "Pretoria"])

print(data)
print("Insert")
data.insert(3, "Mzili")
data.insert(len(data), "The end")
print(data)
