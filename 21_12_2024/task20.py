from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("СОТКАПЛЗ", repeat=5):
    n += 1
    s = "".join(s)

    if all([s[-1] != i for i in "ОА"]) and "ЗЛО" not in s and len(s) == len(set(s)):
        k += 1

print(k)

# Ответ: 5008
