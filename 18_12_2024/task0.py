# Определите количество 12-ричных шестизначных чисел в записи которых
# содержится ровно одна цифра "B" и равное количество чётных и нечётных цифр.

# 0123456789AB, A=10, B=11

chentoe = "02468A"
ne_chentoe = "13579B"

from itertools import *

n = 0  # номер комбинации
k = 0  # количество подходящих комбинаций

for s in product("0123456789AB", repeat=6):
    n += 1
    s = "".join(s)

    if s[0] != "0" and s.count("B") == 1 and \
            sum([int(i in chentoe) for i in s]) == sum([int(i in ne_chentoe) for i in s]):
        k += 1

print(k)

# Ответ: 297000
