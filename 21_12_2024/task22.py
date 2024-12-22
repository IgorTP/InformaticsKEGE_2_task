from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("01234", repeat=5):
    n += 1
    s = "".join(s)

    if s[0] != "0" and sum([s.count(i) for i in "024"]) <= 3:  # (1): all([s.count(i) <= 3 for i in "024"])
        k += 1

print(k)

# Ответ: 1744, (1): 2456
