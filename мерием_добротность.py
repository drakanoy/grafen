from sympy import symbols, init_printing, diff, ln
from math import pi

asr1, asr2, asr3, asr4, asr5, t1, t2, t3, t4, t5, a0 = symbols('asr1, asr2, asr3, asr4, asr5, t1, t2, t3, t4, t5, a0')
init_printing(use_unicode=True)

print(diff((-1 * (
        t1 * ln(asr1 / a0) + t2 * ln(asr2 / a0) + t3 * ln(asr3 / a0) + t4 * ln(asr4 / a0) + t5 * ln(asr5 / a0)) / (
                    t1 ** 2 + t2 ** 2 + t3 ** 2 + t4 ** 2 + t5 ** 2)), t2))
dadr = 2.68804 * 10 ** -12
dr = 0.05 * 10 ** -3
dadl = -8.40011 * 10 ** -16
dl = 0.05
dadP = -3.33808 * 10 ** -21
dP = 5033
dadT = 5.60007 * 10 ** -19
dT = 0.1
Δa = ((dadr * dr) ** 2 + (dadl * dl) ** 2 + (dadP * dP) ** 2 + (dadT * dT) ** 2) ** 0.5
print(Δa)
dh = 10 ** -3
ΔΔp = dh * 10 ** 3 * 9.81 / 2 ** 0.5
dλda = 1.29830 * 10 ** 9
dλdΔp = 3.0912 * 10 ** -10
dλdt = 3.16109 * 10 ** -9
dλdv = 2.9082 * 10 ** -3
dλ = ((dλda * Δa) ** 2 + (dλdΔp * ΔΔp) ** 2 + (dλdt * 1) ** 2 + (dλdv * 10 ** -6) ** 2) ** 0.5
print(dλ)
dddT = 2.42792 * 10 ** -13
dddλ = -1.66971 * 10 ** -4
dddP = -7.23615 * 10 ** -16
Δd = ((dddT * dT) ** 2 + (dddλ * dλ) ** 2 + (dddP * dP) ** 2) ** 0.5
print(Δd)
