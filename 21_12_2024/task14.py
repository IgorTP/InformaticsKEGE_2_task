from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("ЯСНОВИДЕЦ", repeat=5):
    n += 1
    s = "".join(s)

    if any([i == s[0] for i in "СНВДЦ"]) and any([i == s[-1] for i in "ЯОИЕ"]) and s.count(s[0]) == 1 and \
            s.count(s[-1]) == 1:
        k += 1

print(k)

# Ответ: 6860
