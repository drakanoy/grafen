import numpy as np
from math import pi
from matplotlib import cm
import matplotlib.pyplot as plt

T2 = [1.2564, 1.2569, 1.2611, 1.2652, 1.2828, 1.3044, 1.3874]
r_t = [0.9, 1.4, 2.4, 3.4, 5.4, 7.4, 12.4]
r = np.arange(0, 12.5, 0.01)
Ia = 0.03373243
g = 9.8
M = 939.41 * 10**-3
m3 = 115.23 * 10 ** -3
l = 0.11529196
I_teor = lambda r: Ia + 2 * m3 * (r * 10 ** -2) ** 2
I_exper = lambda T2: (M * g * l / (4 * pi ** 2)) * T2
I_exp_list = [I_exper(i) for i in T2]
fig, ax = plt.subplots()
# z = np.polyfit(t, I_exp_list, 1)
# p = np.poly1d(z)
# print(p)
# y1 = p(t)
plt.plot(r_t, I_exp_list, '.', label='Экспериментальные точки')
plt.plot(r, I_teor(r), '-r', label='Теоретическая зависимость')
plt.title(label='Зависимость момента инерции физического маятника \n от расстояния между точкой А и грузиками', loc='center', fontweight='regular')
ax.grid()
ax.set_xlabel('расстояние от точки А до грузиков r, см')
ax.set_ylabel('момент инерции, кг * м$^-$$^2$')
plt.legend()
plt.show()
