#
# def fav_colour(**people):
#     for person, colour in people.items():
#         print(f"{person}'s favorite colour is {colour}")
# fav_colour(makhanya="purple", hlumela="red", koza="blue")

# fav_colour(makhanya="purple", hlumela="red", koza="blue", johnathen="silver")
# fav_colour(makhanya="purple")

def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"
    return "Not sure who this is..."


print(special_greeting(David="Hello"))  # Hello David!
print(special_greeting(Bob='hello'))  # Not sure who this is...
print(special_greeting(David='special'))  # You get a special greeting
