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
    return lambda z: a + b / z

l = [0.195,	0.185,	0.175,	0.165,	0.155,	0.145	,0.135	,0.125	,0.115,	0.105]
l_l = np.arange(0.1, 0.2, 0.0001)
p1 = [-0.2,	1.0,	3.2,	5.7,	8.9	,12.0,	16	,19.2,	23.2,	29.6]
p2 = [-0.1	,1.4,	4.1,	6.6,	9.0,	11.9,	15.0,	19.0,	22.8]
p3 = [0.2,	1.8,	4.1	,7.3,	10.7,	13.8,	17.8,	22.3,	27.6,	34.2]
p4 = [0.2,	1.9,	4.3,	7.1	,9.9	,14.0,	17.6,	22.5,	27.3,	33.1]
l11 = [1/i for i in l]
l_l11 = np.arange(5.1, 9.6, 0.001)

fig, ax = plt.subplots()
z = np.polyfit(l11, p1, 1)
p1_1 = np.poly1d(z)

z = np.polyfit(l11[0:-1], p2, 1)
p2_2 = np.poly1d(z)

z = np.polyfit(l11, p3, 1)
p3_3 = np.poly1d(z)

z = np.polyfit(l11, p4, 1)
p4_4 = np.poly1d(z)


plt.plot(l11, p1, '.', label='T = 27.0 ℃', color='blue')
plt.plot(l_l11, p1_1(l_l11), label='первая аппроксимация', color='blue')
plt.plot(l11[0:-1], p2, '.', label='T = 30.2 ℃', color='red')
plt.plot(l_l11, p2_2(l_l11), label='вторая аппроксимация', color='red')
plt.plot(l11, p3, '.', label='T = 39.9 ℃', color='yellow')
plt.plot(l_l11, p3_3(l_l11), label='третья аппроксимация', color='yellow')
plt.plot(l11, p4, '.', label='T = 48.8 ℃', color='green')
plt.plot(l_l11, p4_4(l_l11), label='четвертая аппроксимация', color='green')
plt.legend()
plt.title(label='P(1/h)',
          loc='center', fontweight='regular')
ax.grid(True)
ax.set_xlabel('1/h, м$^-$$^1$')
ax.set_ylabel('Давление P, кПа')
plt.show()