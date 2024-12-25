from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("0123456", repeat=7):
    n += 1
    s = "".join(s)

    if s[0] != "0" and s[0] != "3" and s[0] != "5" and any([i not in s for i in ("22", "44")]):
        # FIXME (18:12, 23.12.2024): здесь была ошибка: вместо функции any, использовалась all, поэтому ответ был 363416.
        k += 1

print(k)

# Ответ: 466456
