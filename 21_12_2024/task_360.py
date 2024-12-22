from itertools import product

n = 0  # номер
k = 0  # количество
states = []

for s in product("АЕКРТ", repeat=6):
    n += 1
    s = "".join(s)

    if s == "КАРЕТА" or s == "РАКЕТА":
        states.append(n)

n = states[1] - states[0]
print(n)

# Ответ: 3000
