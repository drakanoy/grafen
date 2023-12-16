import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

I = [0, 2, 5, 8, 10, 14, 20, 23, 25]
U = [0, 0.103, 0.25, 0.393, 0.487, 0.68, 0.961, 1.104, 1.207]
# for i in range(len(U)):
#    U[i] = 10 ** 6 * U[i]
fig, ax = plt.subplots()
z, v = np.polyfit(I, U, 1, cov=True)
print(v)  # матрица ковариации
print(v[0][0] ** 0.5)  # корень из диагонального элемента это погрешность коэффициента
# print('asdfsadf', np.polyfit(B, U, 1, cov=True, full=True))
p = np.poly1d(z)
print(p)
plt.plot(I, U, '.', label='Экспериментальные точки')
# plt.errorbar(T, U, yerr=U_pogr, fmt='b.')
plt.plot(I, p(I), '-r', label='Аппроксимация \n $U_{||} = 0.0480 \cdot I$')
plt.title(label='Зависимость продольного напряжения \n от силы тока в $Ge_{n-}$', loc='center',
          fontweight='regular')
ax.grid()
ax.set_xlabel('I, мA')
ax.set_ylabel('$U_{||}$ , В')
plt.legend()
plt.show()

B = [2, 4, 10, 14, 20, 25, 30, 35, 40, 45, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135,
     140, 145, 150, 155, 160, 165, 170]
U = [-28.4, -28, -27, -26.3, -25.2, -24.4, -23.5, -22.8, -21.8, -21, -19.3, -18.6, -17.7, -16.7, -15.9, -15.2, -14.3,
     -13.4, -12.6, -11.7, -10.9, -10, -9.3, -8.4, -7.5, -6.7, -5.8, -5, -4.1, -3.3, -2.6, -1.7, -0.9, 0]
# for i in range(len(U)):
#    U[i] = 10 ** 6 * U[i]
fig, ax = plt.subplots()
z, v = np.polyfit(B, U, 1, cov=True)
print(v)  # матрица ковариации
print(v[0][0] ** 0.5)  # корень из диагонального элемента это погрешность коэффициента
# print('asdfsadf', np.polyfit(B, U, 1, cov=True, full=True))
p = np.poly1d(z)
print(p)
plt.plot(B, U, '.', label='Экспериментальные точки')
# plt.errorbar(T, U, yerr=U_pogr, fmt='b.')
plt.plot(B, p(B), '-r', label='Аппроксимация \n $U_{\perp} = 0.1686 \cdot B - 28.4$')
plt.title(label='Зависимость поперечного напряжения \n от индукции магнитного поля в $Ge_{n-}$', loc='center',
          fontweight='regular')
ax.grid()
ax.set_xlabel('B, мT')
ax.set_ylabel('$U_{\perp}$ , мВ')
plt.legend()
plt.show()

I = [0, 2, 5, 8, 10, 14, 20, 23, 25]
U = [0, 0.157, 0.307, 0.495, 0.609, 0.826, 1.187, 1.372, 1.585]
# for i in range(len(U)):
#    U[i] = 10 ** 6 * U[i]
fig, ax = plt.subplots()
z, v = np.polyfit(I, U, 1, cov=True)
print(v)  # матрица ковариации
print(v[0][0] ** 0.5)  # корень из диагонального элемента это погрешность коэффициента
# print('asdfsadf', np.polyfit(B, U, 1, cov=True, full=True))
p = np.poly1d(z)
print(p)
plt.plot(I, U, '.', label='Экспериментальные точки')
# plt.errorbar(T, U, yerr=U_pogr, fmt='b.')
plt.plot(I, p(I), '-r', label='Аппроксимация \n $U_{||} = 0.0606 \cdot I$')
plt.title(label='Зависимость продольного напряжения \n от силы тока в $Ge_{p+}$', loc='center',
          fontweight='regular')
ax.grid()
ax.set_xlabel('I, мA')
ax.set_ylabel('$U_{||}$ , В')
plt.legend()
plt.show()

B = [2, 4, 10, 14, 20, 25, 30, 35, 40, 45, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135,
     140, 145, 150, 155, 160, 165, 170]
U = [50, 49.7, 48.7, 48.1, 47.2, 46.3, 45.6, 44.7, 44, 43.3, 41.7, 41, 40.2, 39.5, 38.7, 38, 37.3, 36.5, 35.7, 35, 34.2,
     33.5, 32.8, 32, 31.3, 30.6, 29.8, 29.1, 28.4, 27.8, 27.1, 26.4, 25.7, 25]
# for i in range(len(U)):
#    U[i] = 10 ** 6 * U[i]
fig, ax = plt.subplots()
z, v = np.polyfit(B, U, 1, cov=True)
print(v)  # матрица ковариации
print(v[0][0] ** 0.5)  # корень из диагонального элемента это погрешность коэффициента
# print('asdfsadf', np.polyfit(B, U, 1, cov=True, full=True))
p = np.poly1d(z)
print(p)
plt.plot(B, U, '.', label='Экспериментальные точки')
# plt.errorbar(T, U, yerr=U_pogr, fmt='b.')
plt.plot(B, p(B), '-r', label='Аппроксимация \n $U_{\perp} = -0.1491 \cdot B + 50$')
plt.title(label='Зависимость поперечного напряжения \n от индукции магнитного поля в $Ge_{p+}$', loc='center',
          fontweight='regular')
ax.grid()
ax.set_xlabel('B, мT')
ax.set_ylabel('$U_{\perp}$ , мВ')
plt.legend()
plt.show()
