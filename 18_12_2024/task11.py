from itertools import product

n = 0  # номер
k = 0  # количество

d = {"A": 10, "B": 11}

for s in product("0123456789AB", repeat=5):
    n += 1
    s = "".join(s)

    if s[0] != "0" and s.count("A") == 2 and \
            all(["".join(num_and_seven) not in s for num_and_seven in list(zip("02468A", "7" * 6))]) and \
            all(["".join(seven_and_num) not in s for seven_and_num in list(zip("7" * 6, "02468A"))]):
        k += 1

print(k)

# Ответ: 9780
