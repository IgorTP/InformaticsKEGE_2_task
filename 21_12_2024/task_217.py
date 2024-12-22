from itertools import product

n = 0  # номер
k = 0  # количество

# range(7, 0, -1) -> [7, 6, 5, 4, 3, 2, 1]
# Вообще это можно (даже желательно) упростить и сразу внутри первого range() писать "range(4, 6+1, 1)",
# и тогда из условия убрать "len(s) in (4, 5, 6)"

for comb in [product("ЧОАНИМЕ", repeat=i) for i in range(7, 0, -1)]:
    for s in comb:
        n += 1
        s = "".join(s)

        if s.count("М") == 3 and len(s) in (4, 5, 6):
            k += 1

print(k)

# Ответ: 4704
