import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

t = [9.091, 5.935, 4.726]
t.sort()
I_exp = lambda t: 0.013 + (98.75 - 40) * 10 ** -3 * t ** 2
I_exp_list = [I_exp(i) for i in t]
fig, ax = plt.subplots()
z = np.polyfit(t, I_exp_list, 1)
p = np.poly1d(z)
print(p)
y1 = p(t)
plt.plot(t, I_exp_list, '.', label='Экспериментальные точки')
plt.plot(t, y1, '-r', label='квадратичная аппрокисмация')

plt.title(label='Зависимость углового ускорения от массы', loc='center', fontweight='regular')
ax.grid()
ax.set_xlabel('Масса, г')
ax.set_ylabel('Угловое ускорение, с$^-$$^2$')
plt.legend()
plt.show()
