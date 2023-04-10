from sympy import symbols, init_printing, diff, cos
from math import radians
from math import cos as cs
from math import sin as sn


l1, B, l2, t1, t2, r0 = symbols('l1, B, l2, t1, t2, r0')
init_printing(use_unicode=True)

print(diff(B*(l2/t2)**0.5, t2))
