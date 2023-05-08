from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

nu = 1.004 * 10**-6  # кинематическая вязкость м2/с
b = 0.145  # м
a = 0.095  # м

w = np.arange(0, 0.3, 0.001)


q550 = lambda wd: 550 +0* wd
q57 = lambda wd: 57 +0* wd
A = lambda w: w * a**2 * b**2 / (b**2 - a**2)
B = lambda w: -w * a**2 / (b**2 - a**2)



Re = lambda w: (A(w) * np.log(b/a) + 0.5 * B(w) * (b**2-a**2)) / nu


fig, ax = plt.subplots()

plt.plot(w, Re(w), '-r', label='число Рейнольдса')
plt.plot(w, q550(w), '-g', label='верхний предел \n Ω = 0.254 c$^-$$^1$ \n Ω = 1.56 об/мин')
plt.plot(w, q57(w), '-b', label='нижний предел \n Ω = 0.026 c$^-$$^1$ \n Ω = 15.24 об/мин')

plt.title(label='число Рейнольдса', loc='center', fontweight='regular')

ax.grid()
plt.legend()
plt.show()