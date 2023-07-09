'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''


# def extract_full_name(names):
#     return list(name['first']+' '+ name['last'] for name in names)


def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val["first"], val["last"]), l))


names = [{'first': 'Elie', 'last': 'Schoppik'},
         {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))  # ['Elie Schoppik', 'Colt Steele']
