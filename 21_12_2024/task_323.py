from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("01234567", repeat=10):
    n += 1
    s = "".join(s)

    if s[0] != "0" and s.count("7") == 5 and all(["".join(i) not in s for i in zip("1357", "7" * 4)]) and \
            all(["".join(i) not in s for i in zip("7" * 4, "1357")]):
        k += 1

print(k)

# Ответ: 5888
