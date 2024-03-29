import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

t = [9.091, 5.935, 4.726]
r = np.arange(0, 0.3, 0.001)
t.sort()

I0 = 0.02
M = 98.75 * 10**(-3)
k = 0.013
em = 467.7 * 10**(-3)
R_dada = [9 * 10 ** (-2), 14 * 10 ** (-2), 29 * 10 ** (-2)]
I_exper = lambda t: k * (M - 40 * 10**(-3)) * t ** 2
# R = lambda I_exp: ((I_exp - I0) / ((115.32 + 115.15 + 115.46 + 114.77) * 10 ** -3)) ** 0.5
I_teor = lambda r: I0 + (115.32 + 115.15 + 115.46 + 114.77) * 10 ** -3 * r ** 2
R = lambda I: ((I-I0) / ((115.32 + 115.15 + 115.46 + 114.77) * 10 ** -3)) ** 0.5
R_t = lambda t: ((t**2 * k * (58.75 * 10**(-3)) - I0) / em)  **0.5
print(R_t(5.2))
R_list = [R_t(i) for i in t]
print(R_list)
# print(R_list)
I_exper_list = [I_teor(R_t(i)) for i in t]
print(I_exper_list)

# r.sort()

fig, ax = plt.subplots()
z = np.polyfit(R_dada, I_exper_list, 2)
p = np.poly1d(z)
print(p)
y1 = p(R_dada)
plt.plot(r, I_teor(r), '-r', label='Теоретическая зависимость')
plt.plot(R_dada, I_exper_list, '.', label='Экспериментальные точки')
plt.title(label='Зависимость момента инерции  \n от расстояния грузиков до центра барабана', loc='center', fontweight='regular')
ax.grid()
ax.set_xlabel('Удаленность грузиков от центра м')
ax.set_ylabel('Момент инерции кг * м$^2$')
plt.legend()
plt.show()
for i in [29, 14, 9]:
    print(I_teor(i * 10 ** (-2)))