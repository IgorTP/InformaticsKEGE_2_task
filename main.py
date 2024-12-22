from itertools import product, permutations


def impl(a, b):
    return not (a) or b


def f(x, y, z, w):
    return (impl(x, y) or not(impl(z, w))) and (impl(w, not(x)) or impl(not(y), z))


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(0, 0, 0, a1), (0, a2, 1, a3), (0, 0, a4, 1)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(*p, sep='')
