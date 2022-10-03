import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

t = [9.091, 5.935, 4.726]
r = np.arange(0, 30, 0.01)


I0 = 0.02
M = 98.75 * 10**(-3)
k = 0.013
I_exper = lambda t: k *(M - 40 * 10**(-3)) * t ** 2
R = lambda I_exp: ((I_exp - I0) / ((115.32 + 115.15 + 115.46 + 114.77) * 10 ** -3)) ** 0.5
I_teor = lambda r: I0 + (115.32 + 115.15 + 115.46 + 114.77) * 10 ** -3 * r ** 2

R_list = [R(I_exper(i)) for i in t]
print(R_list)
I_exper_list = [I_teor(R(i)) for i in t]
t.sort()
r.sort()

fig, ax = plt.subplots()
# z = np.polyfit(x, y, 2)
# p = np.poly1d(z)
# print(p)
# y1 = p(x)
plt.plot(R_list, I_exper_list, '.', label='Экспериментальные точки')
plt.plot(r, I_teor(r), '-r', label='теоретическая зафисимость')


plt.title(label='Зависимость момента инерции от расстояние грузиков от центра', loc='center', fontweight='regular')
ax.grid()
ax.set_xlabel('Расстояние грузиков от центра, м')
ax.set_ylabel('Момент инерции, кг/м$^2$')
plt.legend()
plt.show()
