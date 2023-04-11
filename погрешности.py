from sympy import symbols, init_printing, diff, cos
from math import radians
from math import cos as cs
from math import sin as sn


q0, r, A = symbols('q0, r, A')
init_printing(use_unicode=True)

print(diff(q0*(1+A/r)**(-1.5), r))
