from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("0123456", repeat=7):
    n += 1
    s = "".join(s)

    if s[0] != "0" and s[0] != "3" and s[0] != "5" and all([i not in s for i in ("22", "44")]):
        k += 1

print(k)

# Ответ: 363416
