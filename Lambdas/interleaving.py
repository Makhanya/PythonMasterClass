def interleave(x, y):
    return "".join(''.join(c) for c in (zip(x, y)))


print(interleave('hi', 'ha'))    # 'hhia'
print(interleave('aaa', 'zzz'))  # 'azazaz'
print(interleave('lzr', 'iad'))  # 'lizard'
