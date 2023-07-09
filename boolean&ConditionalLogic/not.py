age = 78
# 2-8 2 dollar ticket
# 65 5 dollar ticket
# 10 dollars for everyone else
if not ((age >= 2 and age <= 8) or age >= 65):
    print("You pay 10 dollars you are not a child or senior!")
else:
    print("You are a Child or Senior")
