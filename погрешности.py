from sympy import symbols, init_printing, diff, cos
from math import radians
from math import cos as cs
from math import sin as sn


l, a, M, m, g, x = symbols('l, a, M, m, g, x')
init_printing(use_unicode=True)

print(diff((1 + M / m) * (x * g * l * (1 - cos(a))) ** 0.5, a))
y1 = 4.28657 * 10 ** -7
y2 = 4.34650 * 10 ** -7
y3 = 4.46932 * 10 ** -7
y4 = 4.36230 * 10 ** -7
ysr = (y1 + y2 + y3 + y4) / 4

Δycl = (1/4 * ((y1 - ysr) ** 2 + (y2 - ysr) ** 2 + (y3 - ysr) ** 2 + (y4 - ysr) ** 2)) ** 0.5 / (3) ** 0.5 * 2.35
print(Δycl)
print((Δycl ** 2 + (0.719295 * 10**-7) ** 2) ** 0.5)
