import numpy as np
from math import pi
from matplotlib import cm
import matplotlib.pyplot as plt

M_R = [0.0082, 0.0116, 0.0123]
M_r = [0.0066, 0.0078, 0.0050]
I_R = [0.06, 0.06, 0.06]
I_r = [0.1, 0.07, 0.07]
m = [49.287, 98.573, 147.860]
m_n = np.arange(49, 150, 0.001)
fig, ax = plt.subplots()

z = np.polyfit(m, M_R, 1)
p = np.poly1d(z)
print(p)
y1 = p(m_n)
plt.plot(m, M_R, '.', label='Экспериментальные точки')
plt.errorbar(m, M_R, yerr=[0.0019, 0.0019, 0.004], fmt='b.')
#plt.errorbar(m, M_r, yerr=[0.0015, 0.005, 0.013], fmt='b.')
#plt.errorbar(m, I_R, yerr=[0.003, 0.003, 0.004], fmt='b.')
#plt.errorbar(m, I_r, yerr=[0.04, 0.009, 0.009], fmt='b.')
plt.plot(m_n, p(m_n), '-g', label='Линейная аппроксимация')
plt.title(label='Зависимость момента силы трения \n от массы грузика',
          loc='center', fontweight='regular')
ax.grid()
ax.set_xlabel('Масса, г')
ax.set_ylabel('Момент силы трения, Н*кг')
plt.legend()
plt.show()
#a = (0.0018284771950294 / 2**0.5 * 2.92)
#print((0.0016**2+a**2)**0.5)