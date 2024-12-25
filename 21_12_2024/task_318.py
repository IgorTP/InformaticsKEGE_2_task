from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("01234567", repeat=6):
    n += 1
    s = "".join(s)

    if s[0] != "0" and all([s[0] < i and s[1] < i for i in s[2::]]) and \
            all(["".join(i) not in s for i in product("0246", repeat=3)]):
        # FIXME (18:57, 23.12.2024): была исправлена логика проверки количества трёх подряд идущих чётных цифр.
        #  вместо all([i*3 not in s for i in "0246"]) => all(["".join(i) not in s for i in product("0246", repeat=3)])
        #  так как наст НЕ устраивают подобные варианты: "000", "002", "004", "006", "020", "022", "024", "026", "040", ...
        k += 1

print(k)

# Ответ: 5528
