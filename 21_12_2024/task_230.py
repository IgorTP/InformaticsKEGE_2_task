from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("012345678", repeat=7):
    n += 1
    s = "".join(s)

    if s[0] != "0" and s[0] != "3" and s[0] != "7" and all([i * 2 not in s for i in "012345678"]):
        k += 1

print(k)

# Ответ: 1572864
