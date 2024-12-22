from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("012345678", repeat=7):
    n += 1
    s = "".join(s)

    if s[0] != "0" and s.count("6") == 1 and \
            all(["".join(i) not in s for i in product("02468", repeat=2)]) and \
            all(["".join(i) not in s for i in product("1357", repeat=2)]):
        k += 1

print(k)

# Ответ: 25600
