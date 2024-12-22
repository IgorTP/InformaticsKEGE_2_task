from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("0123456789ABCDEF", repeat=5):
    n += 1
    s = "".join(s)

    if s[0] != "0" and s == "".join(sorted(s)):
        k += 1

print(k)

# Ответ: 11628
