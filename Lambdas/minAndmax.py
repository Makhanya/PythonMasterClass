"""
    Max
        Return the largest item in a iterable or the largest of
        two or more arguments
        
        # max (strings, dicts with same keys)

        print(max([3, 4, 1, 2]))  # 4
        print(max([1, 2, 3, 4]))  # 4
        print(max(["awesome"]))  # w
        print(max({1: 'a', 3: 'c', 2: 'b'}))  # 3
       
        """
# nums = [40, 32, 6, 5, 10]
# print(nums)
# print(f"The maximum number in nums {max(nums)}")
# print(f"The minimum number in nums {min(nums)}")

# print(f"max in 'Hello World' - {max('hello wordl')}")
# print(f"min in 'Hello World' - {min('Hello World')}")

# names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
# print(names)
# print(f"Min in names - {min(names)}")
# print(f"Max in names - {max(names)}")
# print(min(len(name)for name in names))
# print([len(name) for name in names])

# print(max(names, key=lambda n: len(n)))
# print(min(names, key=lambda n: len(n)))

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

#print(max(songs, key=lambda s: s['playcount']))
print(max(songs, key=lambda s: s['playcount'])['title'])
