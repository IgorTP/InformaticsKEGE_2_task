from itertools import product

n = 0  # номер
k = 0  # количество

d = {"A": 10, "B": 11}

for s in product("0123456789AB", repeat=5):
    n += 1
    s = "".join(s)

    if s[0] != "0" and s.count("7") == 1 and sum([int(int(i if i in "0123456789" else d[i]) > 8) for i in s]) <= 3:
        k += 1

print(k)

# Ответ: 67476
