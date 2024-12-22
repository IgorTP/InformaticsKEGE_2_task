from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("РЕЖИМДНО", repeat=6):
    n += 1
    s = "".join(s)

    if any([i == s[0] for i in "РЖМДН"]) and any([i == s[1] for i in "ЕИО"]) and any([i == s[-1] for i in "ЕИО"]) and \
            len(s) == len(set(s)):
        k += 1

print(k)

# Ответ: 1800
