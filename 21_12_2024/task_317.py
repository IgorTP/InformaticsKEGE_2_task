from itertools import product

n = 0  # номер
k = 0  # количество


def is_valid(string):
    indexes = [i for i in range(len(string)) if string[i] in "ОЕА"]  # получаем индексы всех гласных букв в строке
    counter = 0

    # создаём цикл, который будет бегать по всем индексам массива indexes, от 0 до len(indexes)-1
    for j in range(0, len(indexes) - 1):

        # обращаемся к j-элементу и j+1, получая пару индексов двух гласных букв
        start, stop = indexes[j], indexes[j + 1]

        # выбираем из строки все буквы стоящие между j-ой гласной и j-ой + 1
        new_string = string[start + 1: stop]

        # если сумма количества вхождений каждой из согласных букв ("КНФТ") в новую строку больше или равно 1
        if sum([new_string.count(k) for k in "КНФТ"]) >= 1:
            counter += 1

    # если это условие выполняется для каждой пары гласных букв
    if counter == len(range(0, len(indexes) - 1)):
        return True
    return False


for s in product("КОНФЕТА", repeat=5):
    n += 1
    s = "".join(s)

    if sum([s.count(i) for i in "ОЕА"]) >= 2 and is_valid(s):
        # FIXME (18:41, 23.12.2024): полностью переписана логика обработки строк, создана отдельная функция.
        k += 1

print(k)

# Ответ: 3888
