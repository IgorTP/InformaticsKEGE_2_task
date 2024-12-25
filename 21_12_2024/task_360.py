from itertools import product

n = 0  # номер
k = 0  # количество
states = []

for s in product("АЕКРТ", repeat=6):
    n += 1
    s = "".join(s)

    if s == "КАРЕТА" or s == "РАКЕТА":
        states.append(n)

# FIXME (19:11, 23.12.2024): переписана логика вывода ответа, так как нужно узнать количество чисел между числом n и m,
#  (m > n) то оно будет равно m - n - 1.
n = states[1] - states[0] - 1
print(n)

# Ответ: 2999
