import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

U = [0.263, 0.336, 0.448, 0.5986, 0.7731, 0.8765, 0.96, 1.0527, 1.12, 1.185, 1.21, 1.22, 1.22, 1.21, 1.19, 1.16, 1.13,
     1.09, 1.06, 1.02]
T = [145, 135, 125, 115, 105, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30]
for i in range(len(T)):
    T[i] = 1 / (T[i] + 273)
for i in range(len(U)):
    U[i] = np.log(    (20 * 10**-3 / (U[i]))      * 0.01/(20*10**-6) )
U_pogr = [0.01] * len(U)
fig, ax = plt.subplots()
print('u', U)
z, v = np.polyfit(T[0:6], U[0:6], 1, cov=True)
print(v) # матрица ковариации
print(v[0][0]**0.5)# корень из диагонального элемента это погрешность коэффициента
print('asdfsadf', np.polyfit(T[0:6], U[0:6], 1, cov=True, full=True))
p = np.poly1d(z)
print(p)
plt.plot(T, U, '.', label='Экспериментальные точки')
#plt.errorbar(T, U, yerr=U_pogr, fmt='b.')
plt.plot(T[0:10], p(T[0:10]), '-r', label='Аппроксимация \n ln(σ) = -4219 (1/T) + 13.72')
plt.title(label='Зависимость логарифма удельной проводимости \n от обратной температуры', loc='center',
          fontweight='regular')
ax.grid()
ax.set_xlabel('1/T,1/K')
ax.set_ylabel('ln(σ)')
plt.legend()
plt.show()
print(4219 * 2 * 8.617 * 10**-5) # энергия гэпа