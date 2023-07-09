def combine_words(word, **kwargs):
    if kwargs:
        if "prefix" in kwargs:
            for x in kwargs:
                return kwargs[x]+word
        if 'suffix' in kwargs:
            for y in kwargs:
                return word+kwargs[y]
    else:
        return word


print(combine_words("child"))  # 'child'
print(combine_words("child", prefix="man"))  # 'manchild'
print(combine_words("child", suffix="ish"))  # 'childish'
print(combine_words("work", suffix="er"))  # 'worker'
print(combine_words("work", prefix="home"))  # 'homework'
