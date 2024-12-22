from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("0123456789", repeat=6):
    n += 1
    s = "".join(s)

    if s[0] != "0" and len(s) == len(set(s)) and \
            (all(["".join(j) not in s for j in product("0246", repeat=2)]) or  # (1): and
             all(["".join(j) not in s for j in product("1357", repeat=2)])):
        k += 1

print(k)

# Ответ: 104544, (1): 26376
