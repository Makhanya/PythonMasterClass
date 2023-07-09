# def current_beat():
#     max = 100
#     nums = (1, 2, 3, 4)
#     i = 0
#     result = []
#     while len(result) < max:
#         if i >= len(nums): i = 0
#         result.append(nums[i])
#         i += 1
#     return result

def current_beat():
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1

b = current_beat()
for x in range(15):
    print(next(b))
# print(current_beat())

# def play_kick_drum()
# if current_beat() ==1
#     play_sount()
