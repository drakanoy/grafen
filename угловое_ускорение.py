import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

x = [40, 49.51, 98.75, 98.62, 147.86, 147.73, 196.97]
y = [0, 0.25, 1.08, 1.03, 2.20, 2.20, 3.05]
x.sort()
y.sort()

fig, ax = plt.subplots()
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
print(p)
y1 = p(x)
plt.plot(x, y, '.', label='Экспериментальные точки')
plt.plot(x, y1, '-r', label='Линейная аппрокисмация \n ε = 0.02m - 0.8')
plt.plot(40, 0, '*', color='green', label='Экстраполяция для ε = 0')

plt.title(label='Зависимость углового ускорения от массы', loc='center', fontweight='regular')
ax.grid()
ax.set_xlabel('Масса, г')
ax.set_ylabel('Угловое ускорение, с$^-$$^2$')
plt.legend()
plt.show()
