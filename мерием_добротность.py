from sympy import symbols, init_printing, diff, ln
from math import pi
asr1, asr2, asr3, asr4, asr5, t1, t2, t3, t4, t5, a0 = symbols('asr1, asr2, asr3, asr4, asr5, t1, t2, t3, t4, t5, a0')
init_printing(use_unicode=True)

# print(diff((-1 * (
#         t1 * ln(asr1 / a0) + t2 * ln(asr2 / a0) + t3 * ln(asr3 / a0) + t4 * ln(asr4 / a0) + t5 * ln(asr5 / a0)) / (
#                     t1 ** 2 + t2 ** 2 + t3 ** 2 + t4 ** 2 + t5 ** 2)), t2))
t1 = 1.06
t2 = 2.12
t3 = 3.18
t4 = 4.24
t5 = 5.30
asr1 = 10.3
asr2 = 8
asr3 = 6
asr4 = 4.3
asr5 = 3
a0 = 15
# print('dy/da0 =', (t1/a0 + t2/a0 + t3/a0 + t4/a0 + t5/a0)/(t1**2 + t2**2 + t3**2 + t4**2 + t5**2))
# print()
# print('dy/dsr1 =', -t1/(asr1*(t1**2 + t2**2 + t3**2 + t4**2 + t5**2)))
# print()
# print('dy/dsr2 =', -t2/(asr2*(t1**2 + t2**2 + t3**2 + t4**2 + t5**2)))
# print()
# print('dy/dsr3 =', -t3/(asr3*(t1**2 + t2**2 + t3**2 + t4**2 + t5**2)))
# print()
# print('dy/dsr4 =', -t4/(asr4*(t1**2 + t2**2 + t3**2 + t4**2 + t5**2)))
# print()
# print('dy/dsr5 =', -t5/(asr5*(t1**2 + t2**2 + t3**2 + t4**2 + t5**2)))
# print()
# print('dy/dt1 =', -2*t1*(-t1*ln(asr1/a0) - t2*ln(asr2/a0) - t3*ln(asr3/a0) - t4*ln(asr4/a0) - t5*ln(asr5/a0))/(t1**2 + t2**2 + t3**2 + t4**2 + t5**2)**2 - ln(asr1/a0)/(t1**2 + t2**2 + t3**2 + t4**2 + t5**2))
# print()
# print('dy/dt2 =', -2*t2*(-t1*ln(asr1/a0) - t2*ln(asr2/a0) - t3*ln(asr3/a0) - t4*ln(asr4/a0) - t5*ln(asr5/a0))/(t1**2 + t2**2 + t3**2 + t4**2 + t5**2)**2 - ln(asr2/a0)/(t1**2 + t2**2 + t3**2 + t4**2 + t5**2))
# print()
# print('dy/dt3 =', -2*t3*(-t1*ln(asr1/a0) - t2*ln(asr2/a0) - t3*ln(asr3/a0) - t4*ln(asr4/a0) - t5*ln(asr5/a0))/(t1**2 + t2**2 + t3**2 + t4**2 + t5**2)**2 - ln(asr3/a0)/(t1**2 + t2**2 + t3**2 + t4**2 + t5**2))
# print()
# print('dy/dt4 =', -2*t4*(-t1*ln(asr1/a0) - t2*ln(asr2/a0) - t3*ln(asr3/a0) - t4*ln(asr4/a0) - t5*ln(asr5/a0))/(t1**2 + t2**2 + t3**2 + t4**2 + t5**2)**2 - ln(asr4/a0)/(t1**2 + t2**2 + t3**2 + t4**2 + t5**2))
# print()
# print('dy/dt5 =', -2*t5*(-t1*ln(asr1/a0) - t2*ln(asr2/a0) - t3*ln(asr3/a0) - t4*ln(asr4/a0) - t5*ln(asr5/a0))/(t1**2 + t2**2 + t3**2 + t4**2 + t5**2)**2 - ln(asr5/a0)/(t1**2 + t2**2 + t3**2 + t4**2 + t5**2))
dyda0 = 0.0162825786207468
Δa0 = 0
dydsr1 = -0.00141629905147625
Δa1 = 1.4373
dydsr2 = -0.004070037096282941
Δa2 = 3.0865
dydsr3 = -0.007515036286498524
Δa3 = 3.2556
dydsr4 = -0.014474483323159393
Δa4 = 3.2556
dydsr5 = -0.03256321305300157
Δa5 = 3.2556
dydt1 = -0.00557006508222371
Δt = 0.01
dydt2 = -0.00971432766753766
Δt2 = 0
dydt3 = -0.0161310450519094
Δt3 = 0
dydt4 = -0.0202134907693346
Δt4 = 0
dydt5 = -0.0210786679660540
Δt5 = 0
dy = ((dyda0 * Δa0) ** 2 + (dydsr1 * Δa1) ** 2 +(dydsr2 * Δa2) ** 2 +(dydsr3 * Δa3) ** 2 +(dydsr4 * Δa4) ** 2 +(dydsr5 * Δa5) ** 2 +(dydt1 * Δt) ** 2 +(dydt2 * Δt) ** 2 +(dydt3 * Δt) ** 2 +(dydt4 * Δt) ** 2 +(dydt5 * Δt) ** 2) ** 0.5
print(dy)
# Δγ1 = ((dydsr1 * 1.3972) ** 2 + (dydsr2 * 1) ** 2 + (dydsr3 * 1) ** 2 + (dydsr4 * 1.3972) ** 2 + (dydsr5 * 1) ** 2 +(dydt1 * 0.01) ** 2 +(dydt2 * 0.01) ** 2 +(dydt3 * 0.01) ** 2 +(dydt4 * 0.01) ** 2 +(dydt5 * 0.01) ** 2) ** 0.5
# acr = 4.3
Δω = ((pi * 0.03757/(1.06 * 0.298333 ** 2))**2 + (pi * 0.01/(1.06 ** 2 * 0.298333))**2) ** 0.5
print(Δω)
# q = (1/3 * ((4-acr)**2 +(5-acr)**2 +(4-acr)**2))**0.5
# w = (q / (2) ** 0.5) * 2.92
# print((w ** 2 + 1) ** 0.5)