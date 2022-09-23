import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import pi

fig, ax = plt.subplots()

om = [388.8, 388.5, 387.7, 387.7, 387.7, 388.1, 387.3, 387.3, 387.8, 387.4, 386.3, 387.2, 387.9, 387.3, 387.2, 387,
      388.6,
      387.5, 385.7, 386.8, 387.1, 387.6, 388, 389.2, 386.1, 386.2, 386.6, 387, 388.6, 386.7, 386.8, 386.7, 387.6, 388.1,
      387, 386.8, 387.6, 387.7, 386.8, 387.2, 387.1, 386.4,
      387.8, 389.4, 388.8, 386.9, 387.6, 388.3, 387.9, 387.5]

om.sort()
G = 0.79
x_sred = 387.46
p = lambda x: (1 / (G * (2 * pi) ** 0.5)) * np.exp(-1 * ((x - x_sred) ** 2 / (2 * G ** 2)))
x = np.linspace(384.9, 390.4, 2000)

plt.title(label='Распределение сопротивлений', loc='center', fontweight='regular')
plt.plot(x, p(x), label='нормальное распределение')
ax.grid()
ax.set_xlabel('Сопротивление R, Ом')
ax.set_ylabel('Плотность вероятности ρ, $Ом^-$$^1$')
sns_plot = sns.distplot(om, hist=True, kde=True,
                        bins=7, color='green', label='гистограмма')
sns_plot1 = sns.kdeplot(om, color='red', label='реальное распределение')
plt.legend()
plt.show()
