from itertools import product, permutations

n = 0  # номер
k = 0  # количество

for s in permutations("КЛАБХАУС"):
    n += 1
    s = "".join(s)

    if all([s[i] != s[i + 1] for i in range(0, len(s) - 1)]):
        k += 1

print(k)

# Ответ: 30240
