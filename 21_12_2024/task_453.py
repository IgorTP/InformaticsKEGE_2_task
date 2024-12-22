from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("01234567", repeat=6):
    n += 1
    s = "".join(s)

    if s[0] != "0":
        if s.count("3") == 2 and "33" not in s:
            start, end = [i for i in range(len(s)) if s[i] == "3"]
            if all([int(i) > 3 for i in s[start + 1: end]]):
                k += 1

print(k)

# Ответ: 8116
