'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''


# def make_song(count=99, beverage="soda"):
#     for x in range(count+1):
#         if (count - x) == 0:
#             yield "No more {}".format(beverage)
#         if (count - x) == 1:
#             yield "Only {} bottle of {} left".format((count - x), beverage)
#         if (count-x)>=2:
#             yield "{} bottles of {} on the wall".format((count - x), beverage)

def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)


song = make_song(4, "coke")
for x in range(5):
    print(next(song))
