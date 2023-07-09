'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''


def compact(list):
    list = [x for x in list if x]
    return list


# [1,2, "All done"]
print(compact([0, 1, 2, "", [], False, {}, None, "All done"]))
