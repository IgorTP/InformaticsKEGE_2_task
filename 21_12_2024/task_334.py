from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("0123456789ABC", repeat=8):
    n += 1
    s = "".join(s)

    if s[0] != "0":
        if s.count("А") <= 2:
            if len(s) - len(set(s)) == 6:
                k += 1

print(k)

# Ответ:
