'''
sevens = get_unlimited_multiples(7)
[next(sevens) for i in range(15)]
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
[next(ones) for i in range(20)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''


# def get_unlimited_multiples(num=1):
#     for x in range(1000000):
#         if x != 0:
#             if x % num == 0:
#                 yield x

def get_unlimited_multiples(num=1):
    next_num = num
    while True:
        yield next_num
        next_num += num


# four = get_unlimited_multiples(4)
# for x in range(20):
#     print(next(four))
seven = get_unlimited_multiples(7)
for x in range(15):
    print(next(seven))
