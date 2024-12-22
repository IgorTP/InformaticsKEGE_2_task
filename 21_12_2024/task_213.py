from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("ТЬЮРИНГ", repeat=6):
    n += 1
    s = "".join(s)

    if s[0] != "Ь" and all(["".join(i) not in s for i in zip("ЮИ", "Ь" * 2)]) and len(s) == len(set(s)):
        k += 1

print(k)

# Ответ: 3120
