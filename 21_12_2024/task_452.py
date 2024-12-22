from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("012345678", repeat=7):
    n += 1
    s = "".join(s)

    if s[0] != "0" and s[0] not in "1357" and int(s[-1]) % 3 != 0 and s.count("6") >= 1:
        k += 1

print(k)

# Ответ: 827352
