from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("АБОРСУЭ", repeat=5):
    n += 1
    s = "".join(s)

    if n % 2 == 0 and (s.count("Р") >= 2 and any([f"Р{i}Р" in s for i in "АБОСУЭ"])) and "У" not in s:
        k += 1

print(k)

# Ответ: 235
