from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("01234567", repeat=6):
    n += 1
    s = "".join(s)

    if s[0] != "0" and all([s[0] < i and s[1] < i for i in s[2::]]) and all([i * 3 not in s for i in "0246"]):
        k += 1

print(k)

# Ответ: 7156
