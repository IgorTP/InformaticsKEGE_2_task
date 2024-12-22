from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("БВЕЙОР", repeat=5):
    n += 1
    s = "".join(s)

    if s.count("Й") <= 1 and s[0] != "Й" and s[-1] != "Й" and "ЙЕ" not in s and "ЕЙ" not in s:
        k += 1

print(k)

# Ответ: 4325
