from itertools import product

n = 0  # номер
k = 0  # количество
ns = []

for s in product("ЁИКЛНОС", repeat=5):
    n += 1
    s = "".join(s)

    if s.count("Ё") >= 2 and s[0] != "О" and s[1] == "К":
        k += 1
        ns.append(n)

print(ns[-1])

# Ответ: 15387
