from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("01234567", repeat=4):
    n += 1
    s = "".join(s)

    if s[0] != "0" and any([s[0] == i for i in "0246"]) and s == "".join(sorted(s, reverse=True)):
        k += 1

print(k)

# Ответ: 129
