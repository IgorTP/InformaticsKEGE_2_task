from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("МЕЧТА", repeat=6):
    n += 1
    s = "".join(s)

    if s.count("А") >= 3:
        k += 1

print(k)

# Ответ: 1545
