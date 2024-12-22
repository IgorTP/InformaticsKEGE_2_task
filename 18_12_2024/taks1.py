from itertools import product

n = 0  # номер
k = 0  # количество

evens = "13579B"
not_evens = "02468A"

for s in product("0123456789AB", repeat=6):
    n += 1
    s = "".join(s)

    if s[0] != "0" and s.count("B") == 1 and \
            sum([(1 if i in evens else 0) for i in s]) == sum([(1 if i in not_evens else 0) for i in s]):
        k += 1

print(k)

# Ответ: 297000
