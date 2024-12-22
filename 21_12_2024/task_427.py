from itertools import product

n = 0  # номер
k = 0  # количество
ns = []

for s in product("ГЕНОСТХЮ", repeat=4):
    n += 1
    s = "".join(s)

    if s.count("О") >= 2 and "С" not in s and n % 2 != 0:
        k += 1
        ns.append(n)

print(ns[-1])

# Ответ: 3807
