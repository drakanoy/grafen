import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

B = [ 56, 155, 257, 356, 456, 555, 656, 756, 856, 956, 1055]
U = [ 0.0000009, 0.0000011, 0.0000017, 0.0000023, 0.0000027, 0.0000034, 0.0000039, 0.0000044, 0.0000047, 0.0000051,
     0.0000056]
for i in range(len(U)):
    U[i] = 10**6*U[i]
fig, ax = plt.subplots()
z, v = np.polyfit(B, U, 1, cov=True)
print(v)  # матрица ковариации
print(v[0][0] ** 0.5)  # корень из диагонального элемента это погрешность коэффициента
# print('asdfsadf', np.polyfit(B, U, 1, cov=True, full=True))
p = np.poly1d(z)
print(p)
plt.plot(B, U, '.', label='Экспериментальные точки')
# plt.errorbar(T, U, yerr=U_pogr, fmt='b.')
plt.plot(B, p(B), '-r', label='Аппроксимация \n $U_{\perp} = 4.902 \cdot 10^{-6} B + 5.3 \cdot 10^{-7}$')
plt.title(label='Зависимость поперечного напряжения \n от индукции магнитного поля', loc='center',
          fontweight='regular')
ax.grid()
ax.set_xlabel('B, мТл')
ax.set_ylabel('$U_{\perp}$ , мкВ')
plt.legend()
plt.show()

