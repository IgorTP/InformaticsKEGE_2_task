from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("0123456789ABCDEF", repeat=12):
    n += 1
    s = "".join(s)

    if s[0] != "0" and s == "".join(sorted(s, reverse=True)) and \
            all([s[i] % 2 != s[i + 1] % 2 for i in range(0, len(s) - 1)]):
        k += 1

print(k)

# Ответ: 102
