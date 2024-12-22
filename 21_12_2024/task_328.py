from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("СВЯТОСЛАВ", repeat=7):  # (1): СВЯТОЛА
    n += 1
    s = "".join(s)

    if sum([s.count(i) for i in "ЯОА"]) > sum([s.count(i) for i in "СВТЛ"]):
        k += 1

print(k)

# Ответ: 828873, (1): 285687
