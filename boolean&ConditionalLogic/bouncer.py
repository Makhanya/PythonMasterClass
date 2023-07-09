# ask for age
print("This is the age app")
# age = input("How old are you: ")
# age = int(age)
# if age != "":
#     if 18 <= age < 21:  # 18-21 wristband
#         print("You can enter, but need a wristband!")
#     elif age >= 21:  # 21+ drink, normal entry
#         print("You are good to enter and can drink!")
#     else:  # too young, sorry
#         print("You cant came in little one!")
# else:
#     print("Please enter an age!")

age = input("How old are you: ")
age = int(age)
if age:
    if age >= 21:
        print("You are good to enter and can drink!")
    elif age >= 18:
        print("You can enter, but you need a wristband!")
    else:
        print("You can't come in, little one!")
else:
    print("Please enter an age!")
