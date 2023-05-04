import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

l = [60, 75, 115, 138, 170, 196]
T = [84, 83, 82, 81, 80, 79]
T_pogr = [1]*len(T)
l_pogr = [1]*len(l)
T.sort()
fig, ax = plt.subplots()
z = np.polyfit(T, l, 1)
p = np.poly1d(z)
print(p)
plt.plot(T, l, '.', label='Экспериментальные точки')
plt.errorbar(T, l, xerr=T_pogr, yerr=l_pogr, fmt='b.')
plt.plot(T, p(T), '-r', label='Аппроксимация')
plt.title(label='Зависимость объема жидкости на единицу длины \n от температуры газа', loc='center', fontweight='regular')
ax.grid()
ax.set_xlabel('T, ℃')
ax.set_ylabel('l, мм')
plt.legend()
plt.show()
