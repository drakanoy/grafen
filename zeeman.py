import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0.25, 0.3]
D = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1647797823, 0.2318010307, 0.3383946958]
B1 = [0.2, 0.25, 0.3]
D1 = [0.1647797823, 0.2318010307, 0.3383946958]
fig, ax = plt.subplots()
z, v = np.polyfit(B, D, 1, cov=True)
print(v)  # матрица ковариации
print(v[0][0] ** 0.5)  # корень из диагонального элемента это погрешность коэффициента
# print('asdfsadf', np.polyfit(B, U, 1, cov=True, full=True))
p = np.poly1d(z)
print(p)
plt.plot(B1, D1, '.', label='Экспериментальные точки')
# plt.errorbar(T, U, yerr=U_pogr, fmt='b.')
plt.plot(B, p(B), '-r', label='Аппроксимация \n $\delta/\Delta = 1 \cdot B$')
plt.title(label='Зависимость отношения дифференциальных элементов площади \n от индукции магнитного поля', loc='center',
          fontweight='regular')
ax.grid()
ax.set_xlabel('$B$ , Тл')
ax.set_ylabel('$\delta/\Delta$')
plt.legend()
plt.show()
