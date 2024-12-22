from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("0123456789ABCDEF", repeat=8):
    n += 1
    s = "".join(s)

    if s[0] != "0":
        if sum([s.count(i) for i in "02468ACE"]) == 3:
            k += 1

print(k)

# Ответ: 895483904
