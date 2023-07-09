'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''


def list_manipulation(list, cdr, pos, value=None):
    if "remove" in cdr:
        if "end" in pos:
            return list.pop()
        elif "beginning" in pos:
            return list.pop(0)
    if "add" in cdr:
        if "beginning" in pos:
            list.insert(0, value)
            return list
        elif "end" in pos:
            list.append(value)
            return list


print(list_manipulation([1, 2, 3], "remove", "end"))  # 3
print(list_manipulation([1, 2, 3], "remove", "beginning"))  # 1
print(list_manipulation([1, 2, 3], "add", "beginning", 20))  # [20,1,2,3]
print(list_manipulation([1, 2, 3], "add", "end", 30))  # [1,2,3,30]
