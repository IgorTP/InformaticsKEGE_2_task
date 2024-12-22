from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("01234567", repeat=7):
    n += 1
    s = "".join(s)

    # Алгоритм для проверки, что 2 чётные не стоят рядом и 2 нечётные не стоят рядом, то есть:
    # ("00", "02", ... not in s) and ("11", "13", ... not in s)
    if s[0] != "0" and len(s) == len(set(s)) and \
            all(["".join(j) not in s for j in product("0246", repeat=2)]) and \
            all(["".join(j) not in s for j in product("1357", repeat=2)]):
        k += 1

print(k)

# Ответ: 1008
