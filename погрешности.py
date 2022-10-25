from sympy import symbols, init_printing, diff, sin

a1, a2, t1, t2 = symbols('a1, a2, t1, t2')
init_printing(use_unicode=True)

print(diff((a1 ** 2 - a2 ** 2) / (a1 * t1 ** 2 - a2 * t2 ** 2), a1))
print(diff((a1 ** 2 - a2 ** 2) / (a1 * t1 ** 2 - a2 * t2 ** 2), a2))
print(diff((a1 ** 2 - a2 ** 2) / (a1 * t1 ** 2 - a2 * t2 ** 2), t1))
print(diff((a1 ** 2 - a2 ** 2) / (a1 * t1 ** 2 - a2 * t2 ** 2), t2))

print()
print()
print(diff(a1 / t1 ** 2, t1))