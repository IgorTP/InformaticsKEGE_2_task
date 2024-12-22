from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("0123456789ABCDEFGHIJKLMNOPQRST", repeat=7):
    n += 1
    s = "".join(s)

    if s[0] != "0":
        if s.count("B") == 2:
            if all((i * 2 not in s for i in "0123456789ABCDEFGHIJKLMNOPQRST")):
                k += 1

print(k)

# Ответ:
