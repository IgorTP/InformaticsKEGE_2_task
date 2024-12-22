from itertools import product

n = 0  # номер
k = 0  # количество

from itertools import zip_longest

for s in product("КОНФЕТА", repeat=5):
    n += 1
    s = "".join(s)

    if sum([s.count(i) for i in "ОЕА"]) >= 2:
        d = {s.index(j): j for j in s}
        glasnie_indexes = {k: v for k, v in d.items() if v in "ОЕА"}
        lst = list(glasnie_indexes.keys())

        if len(lst) > 1:
            for val1, val2 in zip_longest(lst[::2], lst[1::2], fillvalue=lst[-2]):
                if val1 > val2:
                    val1, val2 = val2, val1

                for l in range(val1, val2):
                    if s[l] in "КНФТ":
                        k += 1
                        break

print(k)

# Ответ: 5136
