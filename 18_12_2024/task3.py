from itertools import product

n = 0  # номер
k = 0  # количество

z1 = [product("ЛРСТ", repeat=j) for j in range(4, 0, -1)]
z2 = [["".join(j) for j in list(i)] for i in z1]

for s in product("АЛРСТЮ", repeat=5):
    n += 1
    s = "".join(s)

    if s.count("Ю") <= 2 and all([all([not s.endswith(j) for j in i]) for i in z2]):
        k += 1

print(k)

# Ответ: 2400
