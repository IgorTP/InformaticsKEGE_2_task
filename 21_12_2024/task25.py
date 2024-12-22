from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("0123456", repeat=5):
    n += 1
    s = "".join(s)

    sum_s = sum(map(int, s))
    if s[0] != "0" and sum([s.count(i) for i in "0246"]) >= 3 and sum([sum_s % i == 0 for i in range(1, 6 + 1)]) == 2:
        k += 1

print(k)

# Ответ: 2006
