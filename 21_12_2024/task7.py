from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("АКЛОШ", repeat=5):
    n += 1
    s = "".join(s)

    if sum([i in "АО" for i in s]) >= 1:
        k += 1

print(k)

# Ответ: 2882
