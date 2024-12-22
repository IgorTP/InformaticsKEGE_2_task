from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("БЕМОЪ", repeat=4):
    n += 1
    s = "".join(s)

    if s.count("О") == 1 and s[0] != "Ъ" and s[-1] != "Ъ":
        k += 1

print(k)

# Ответ: 168
