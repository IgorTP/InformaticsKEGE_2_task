from itertools import product

n = 0
k = 0

for s in product("АКЛМРС", repeat=6):
    n += 1
    s = "".join(s)

    conds = 0

    # 1st condition
    comb_dict = {let: s.count(let) for let in s}
    repeated_let = None
    if 3 in comb_dict.values():
        conds += 1
        repeated_let = list(comb_dict.keys())[list(comb_dict.values()).index(3)]

    # 2nd condition
    new_s = "".join([i for i in s if i != repeated_let])
    if len(set(new_s)) == len(new_s):
        conds += 1

    # 3rd conditions
    if "КС" in s or "СК" not in s:
        conds += 1

    if conds == 3:
        k += 1
        print(n, s)

    # Debug Info
    # print(f"{n}: {s}, {new_s}, {repeated_let}, {comb_dict}, 1_cond: {3 in comb_dict.values()}, 2_cond: {len(set(new_s)) == len(new_s)}, 3_cond: {'КС' in s or 'СК' not in s}" )
    # if n == 200:
    #     exit(0)

print(f"\nКоличество слов: {k}")
