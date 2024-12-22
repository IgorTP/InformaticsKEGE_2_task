from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("ЕЛОПРСТ", repeat=5):
    n += 1
    s = "".join(s)

    if n % 2 == 1 and s[-1] in "ЕО" and sum([(1 if i in "ЛПРСТ" else 0) for i in s]) <= 3:
        k += 1

print(k)

# Ответ: 1776
