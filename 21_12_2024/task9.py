from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("АВДПР", repeat=4):
    n += 1
    s = "".join(s)

    if sum([i in "А" for i in s]) == 0 and len(s) == len(set(s)):
        k += 1

        print(n)
        break

# Ответ: 195
