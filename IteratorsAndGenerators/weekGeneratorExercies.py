'''
days = week()
next(days) # 'Monday'
next(days) # 'Tuesday'
next(days) # 'Wednesday'
next(days) # 'Thursday'
next(days) # 'Friday'
next(days) # 'Saturday'
next(days) # 'Sunday'
next(days) # StopIteration
'''


# def week():
#     x = 0
#     while x <= 6:
#         if x == 0:
#             yield "Monday"
#         if x == 1:
#             yield "Tuesday"
#         if x == 2:
#             yield "Wednesday"
#         if x == 3:
#             yield "Thursday"
#         if x == 4:
#             yield "Friday"
#         if x == 5:
#             yield "Saturday"
#         if x == 6:
#             yield "Sunday"
#         x += 1

def week():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        yield day


days = week()
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
