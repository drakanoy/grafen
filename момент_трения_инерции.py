import numpy as np
from math import pi
from matplotlib import cm
import matplotlib.pyplot as plt

M_R = [0.0082, 0.0116, 0.0123]
M_r = [0.0066, 0.0078, 0.0050]
I_R = [6, 6, 6]
I_r = [10, 6.6, 7]
m = [49.287, 98.573, 147.860]
m_n = np.arange(49, 150, 0.001)
fig, ax = plt.subplots()

z = np.polyfit(m, I_r, 0)
p = np.poly1d(z)
print(p)
y1 = p(m_n)
plt.plot(m, I_r, '.', label='Экспериментальные точки')
#plt.errorbar(m, M_R, yerr=[0.0019, 0.0019, 0.004], fmt='b.')
#plt.errorbar(m, M_r, yerr=[0.0015, 0.005, 0.013], fmt='b.')
#plt.errorbar(m, I_R, yerr=[2, 1.3, 1], fmt='b.')
plt.errorbar(m, I_r, yerr=[4, 0.6, 0.9], fmt='b.')
plt.plot(m_n, p(m_n), '-g', label='Линейная аппроксимация')
plt.title(label='Линейная зависимость момента инерции \n от массы грузика',
          loc='center', fontweight='regular')
ax.grid()
ax.set_xlabel('Масса, г')
ax.set_ylabel('Момент инерции, кг*м$^2$')
plt.legend()
plt.show()
#print(1.9972133065087 / 2**0.5 * 2.92)
#print((0.0054**2+4.123749771724261**2)**0.5)