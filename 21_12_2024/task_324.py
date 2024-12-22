from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("01234567", repeat=10):
    n += 1
    s = "".join(s)

    if s[0] != "0" and sum([s.count(i) for i in "1357"]) == 3 and all([i * 2 not in s for i in "1357"]):
        k += 1

print(k)

# Ответ:
