import numpy as np
from math import pi
from matplotlib import cm
import matplotlib.pyplot as plt

m_0 = [3.76, 10.72, 11.52]
m = []
for i in m_0:
    m.append(1/(i) ** 0.5)
print(m)
v = [3.71316, 4.83186, 4.67856]
v_n = np.arange(0.2, 0.6, 0.01)
fig, ax = plt.subplots()
z = np.polyfit(m, v, 1)
p = np.poly1d(z)
print(p)
y1 = p(v_n)
plt.plot(v_n, p(v_n), '-g', label='линейная апроксимация')
plt.plot(m, v, '.', label='Экспериментальные точки')
plt.title(label='аааааааа',
          loc='center', fontweight='regular')
ax.grid()
plt.errorbar(m, v, yerr=[1.29551, 1.178975257942788, 1.0422162026790112], fmt='b.')
ax.set_xlabel('1 / корень(масса), гг вп')
ax.set_ylabel('скорость v, м/с')
plt.legend()
plt.show()
