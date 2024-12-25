from itertools import product

n = 0  # номер
k = 0  # количество

for s in product("0123456", repeat=5):
    n += 1
    s = "".join(s)

    sum_s = sum(map(int, s))
    if s[0] != "0" and sum([s.count(i) for i in "0246"]) >= 3 and \
            sum([sum_s % i == 0 for i in range(1, sum_s + 1)]) == 2:
        # FIXME (18:17, 23.12.2024): здесь была ошибка: все делители числа sum_s брались из полуинтервала range(1, 6 + 1),
        #  однако значение sum_s может быть опредённо больше 6, поэтому правильная запись range(1, sum_s + 1), поэтому ответ был 2006.
        k += 1

print(k)

# Ответ: 1986
