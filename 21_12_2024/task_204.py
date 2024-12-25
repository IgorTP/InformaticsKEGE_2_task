from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("0123456789", repeat=6):
    n += 1
    s = "".join(s)

    if s[0] != "0" and len(s) == len(set(s)) and \
            (all(["".join(j) not in s for j in product("02468", repeat=2)]) and
             all(["".join(j) not in s for j in product("13579", repeat=2)])):
        # FIXME (18:00, 23.12.2024): здесь была ошибка: 9 не было в нечётных числах, а 8 в чётных поэтому ответ был 26376.
        k += 1

print(k)

# Ответ: 6480
