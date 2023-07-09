'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''
import random


def return_day(num):
    day = ''
    if num == 1:
        day = "Sunday"
    elif num == 2:
        day = "Monday"
    elif num == 3:
        day = "Tuesday"
    elif num == 4:
        day = "Wednesday"
    elif num == 5:
        day = "Thursday"
    elif num == 6:
        day = "Friday"
    elif num == 7:
        day = "Saturday"
    else:
        day = None

    return day


day = random.randint(0, 7)
print(return_day(day))
