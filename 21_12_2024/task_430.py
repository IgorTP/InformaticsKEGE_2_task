from itertools import product, permutations

n = 0  # номер
k = 0  # количество

for s in product("БЕЧЮ", repeat=5):
    n += 1
    s = "".join(s)

    if n % 2 == 0 and s[0] != "Ю":
        if s[1] != "Е":
            k += 1

print(k)

# Ответ: 288
