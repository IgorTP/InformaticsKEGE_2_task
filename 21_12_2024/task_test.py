from itertools import *

k = set()
for s in product("0123456789ABCDEF", repeat=3):
    s = "".join(s)
    t = ""

    for x in s:
        if x in "02468ACE":
            t += "H"
        else:
            t += "N"

    if s[0] != "0" and len(s) == len(set(s)) and "HH" not in t and "NN" not in t:
        k.add(s)

print(len(k))
