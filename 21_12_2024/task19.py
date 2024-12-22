from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("ПИКАЧУ", repeat=5):
    n += 1
    s = "".join(s)

    if s.count("У") >= 2:
        k += 1

print(k)

# Ответ: 1526
