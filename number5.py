import math


def main(y, x, z):
    n = 8
    i = 1
    summ = 0
    while i <= n:
        summ += 67 * (z[i - 1] ** 2 - x[8 - math.ceil(i / 2)] ** 3 - y[8 - math.ceil(i / 2)]) ** 6
        i += 1
    return summ


print(main([-0.43, -0.24, 0.37, -0.71, 0.24, 0.44, 0.79, -0.6],
           [0.22, 0.75, -0.97, 0.53, 0.65, -0.35, 0.07, -0.72],
           [0.87, 0.41, -0.21, -0.58, -0.16, -0.34, 0.74, -0.35]))
