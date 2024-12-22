from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("01234567", repeat=6):
    n += 1
    s = "".join(s)

    if s[0] != "0":
        if s.count("4") == 2 and "44" not in s:
            start, end = [i for i in range(len(s)) if s[i] == "4"]
            new_lst = [i for i in s if i != "4"]  # числа отличные от 4
            if all([int(i) >= 5 for i in s[start + 1: end]]) and len(new_lst) == len(set(new_lst)):
                k += 1

print(k)

# Ответ: 1614
