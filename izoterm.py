import numpy as np
from math import pi
import matplotlib as mpl
import matplotlib.pyplot as plt
#mpl.rcParams['font.family'] = 'fantasy'

def mnkGP(x, y):  # функция которую можно использзовать в програме
    n = len(x)  # количество элементов в списках
    s = sum(y)  # сумма значений y
    s1 = sum([1 / x[i] for i in range(0, n)])  # сумма 1/x
    s2 = sum([(1 / x[i]) ** 2 for i in range(0, n)])  # сумма (1/x)**2
    s3 = sum([y[i] / x[i] for i in range(0, n)])  # сумма y/x
    a = round((s * s2 - s1 * s3) / (n * s2 - s1 ** 2), 3)  # коэфициент а с тремя дробными цифрами
    b = round((n * s3 - s1 * s) / (n * s2 - s1 ** 2), 3)  # коэфициент b с тремя дробными цифрами
    s4 = [a + b / x[i] for i in range(0, n)]  # список значений гиперболической функции
    so = round(sum([abs(y[i] - s4[i]) for i in range(0, n)]) / (n * sum(y)) * 100, 3)
    return s4

l = [0.195,	0.185,	0.175,	0.165,	0.155,	0.145	,0.135	,0.125	,0.115,	0.105]
l_l = np.arange(0, 0.2, 0.0001)
p1 = [-0.2,	1.0,	3.2,	5.7,	8.9	,12.0,	16	,19.2,	23.2,	29.6]
p2 = [-0.1	,1.4,	4.1,	6.6,	9.0,	11.9,	15.0,	19.0,	22.8]
p3 = [0.2,	1.8,	4.1	,7.3,	10.7,	13.8,	17.8,	22.3,	27.6,	34.2]
p4 = [0.2,	1.9,	4.3,	7.1	,9.9	,14.0,	17.6,	22.5,	27.3,	33.1]
fig, ax = plt.subplots()
#z = np.polyfit(l, p1, -1)
#p1_1 = np.poly1d(z)


#z = np.polyfit(l, p2, -1)
#p2_2 = np.poly1d(z)
plt.plot(l, p1, '.', label='первые точки', color='blue')
plt.plot(l, mnkGP(l, p1), label='первая аппроксимация', color='blue')
plt.plot(l[0:-1], p2, '.', label='вторые точки', color='red')
plt.plot(l[0:-1], mnkGP(l[0:-1], p2), label='вторая аппроксимация', color='red')
plt.plot(l, p3, '.', label='третьи точки', color='yellow')
plt.plot(l, mnkGP(l, p3), label='третья аппроксимация', color='yellow')
plt.plot(l, p4, '.', label='четвертые точки', color='green')
plt.plot(l, mnkGP(l, p4), label='четвертые аппроксимация', color='green')
plt.legend()
plt.title(label='Зависимость давления газа от объема сосуда',
          loc='center', fontweight='regular')
ax.grid(True)
ax.set_xlabel('Высота подъёма поршня h, м')
ax.set_ylabel('Давление P, кПа')
plt.show()