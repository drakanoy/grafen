from sympy import symbols, init_printing, diff, cos
from math import radians
from math import cos as cs
from math import sin as sn


mc = 11.52 * 10 ** -3
ac = radians(15.20)
da_c = radians(3.4076)
l, a, M, m, g, x = symbols('l, a, M, m, g, x')
init_printing(use_unicode=True)

print(diff((1 + M / m) * (x * g * l * (1 - cos(a))) ** 0.5, a))
g = 9.8
x = 2
M = 0.09882 + mc
m = mc
a = ac
l = 0.285
dv_dM_c = (g*l*x*(1 - cs(a)))**0.5/m
print(dv_dM_c)
dv_dm_c = -M*(g*l*x*(1 - cs(a)))**0.5/m**2
print(dv_dm_c)
dv_dl_c = 0.5*(g*l*x*(1 - cs(a)))**0.5*(M/m + 1)/l
print(dv_dl_c)
dv_da_c = 0.5*(g*l*x*(1 - cs(a)))**0.5*(M/m + 1)*sn(a)/(1 - cs(a))
print(dv_da_c)
dm = 0.01 * 10 ** -3
dM = (2) ** 0.5 * dm
dl = (0.001 ** 2 + 0.0005 ** 2) ** 0.5
da = da_c
Δv = ((dv_dM_c * dM) ** 2 + (dv_dm_c * dm) ** 2 + (dv_dl_c * dl) ** 2 + (dv_da_c * da) ** 2) ** 0.5
print()
print(Δv)