from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

nu = 1.004 * 10**6  # кинематическая вязкость м2/с
D = 0.15  # м
d = 0.06  # м
wD = 0
wd = np.arange(0, 100000, 1)


q = lambda wd: 2000 +0* wd
A = lambda wd: 2 * d**2 * D**2 * (wD-wd) / (D**2 - d**2)
B = lambda wd: (D**2 * wD - d**2 * wd) / (D**2 - d**2)


u = lambda wd: -A(wd) * np.log(D/d) / (D-d) + 0.5 * B(wd) * (D+d)  # скорость м/с
Re = lambda wd: u(wd) * (D-d) / nu


fig, ax = plt.subplots()

plt.plot(wd, Re(wd), '-r', label='полезное число Рейнольдса')
#plt.plot(wd, q(wd), '-g', label='gkgfu')
plt.title(label='число Рейнольдса', loc='center', fontweight='regular')

ax.grid()
plt.legend()
plt.show()