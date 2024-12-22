from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("ЬРПЛЕА", repeat=5):
    n += 1
    s = "".join(s)

    if n <= 387 and s[-1] == "Ь":
        k += 1

print(k)

# Ответ: 65
