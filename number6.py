import math


def prod(inter):
    result = 0
    for i in inter:
        result += i
    return result


def main(E):
    H = {(4 * e - e) for e in E if e > -math.inf if e < 51}
    N = {math.ceil(e / 4) for e in E if e > -87 if e < 38}
    I = {abs(v) for v in N if v < 72 if v >= -13}
    b = len(H.union(I)) + prod(q * i for q in H for i in I)
    return b


print(main({-61, 36, 43, 44, -81, 50, -13, -75, 54, -39}))
print(main({-30, 2, -53, 43, -19, -15, -8, 25, 94}))
