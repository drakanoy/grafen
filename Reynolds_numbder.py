from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

nu = 1.004 * 10 ** -6  # кинематическая вязкость м2/с
b = 75 * 10 ** (-3)  # м
a = 49 * 10 ** (-3)  # м

w = np.arange(0, 0.9, 0.001)

Re550 = lambda wd: 550 + 0 * wd
RE57 = lambda wd: 57 + 0 * wd
Ta400 = lambda wd: 400 + 0 * wd
Ta41 = lambda wd: 41.3 + 0 * wd
A = lambda w: w * a ** 2 * b ** 2 / (b ** 2 - a ** 2)
B = lambda w: -w * a ** 2 / (b ** 2 - a ** 2)

Re = lambda w: (A(w) * np.log(b / a) + 0.5 * B(w) * (b ** 2 - a ** 2)) / nu
Ta = lambda w: w ** 2 * a * (b - a) ** 3 / (nu ** 2)

fig, ax = plt.subplots()

#plt.plot(w, Re(w) * ((b - a) / a), '-r', label='мое')
plt.plot(w, (Ta(w))**0.5, '-y', label='Елены')
# plt.plot(w, Re550(w), '-g', label='верхний предел \n Ω = 0.254 c$^-$$^1$ \n Ω = 1.56 об/мин')
# plt.plot(w, Re57(w), '-b', label='нижний предел \n Ω = 0.026 c$^-$$^1$ \n Ω = 15.24 об/мин')
#plt.plot(w, Ta400(w), '-g', label='верхний предел \n Ω = 0.254 c$^-$$^1$ \n Ω = 1.56 об/мин')
plt.plot(w, Ta41(w), '-b', label='нижний предел')

plt.title(label='число Тейлора', loc='center', fontweight='regular')

ax.grid()
plt.legend()
plt.show()
