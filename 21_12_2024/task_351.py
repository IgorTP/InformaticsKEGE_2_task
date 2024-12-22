from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("ЕСТВО", repeat=8):
    n += 1
    s = "".join(s)

    if sum([s.count(i) for i in "ЕО"]) >= 3 and sum([s.count(i) for i in "СТВ"]) >= 4 and \
            all([i * 2 not in s for i in "ЕО"]):
        k += 1

print(k)

# Ответ: 107406
