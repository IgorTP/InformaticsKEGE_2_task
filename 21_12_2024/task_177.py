from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("ДЖОБС", repeat=6):
    n += 1
    s = "".join(s)

    if all([s.count(i) == 1 for i in "ДОС"]) and s.count("Ж") <= 2:
        k += 1

print(k)

# Ответ: 840
