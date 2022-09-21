import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import pi

fig, ax = plt.subplots()

massy = [4.47, 4.38, 4.52, 5.08, 4.72, 4.51, 4.41, 4.42, 4.67, 4.6, 4.52, 4.15, 4.45, 4.87, 4.48, 4.46, 4.47, 4.48,
         4.46, 4.49, 4.4, 4.53, 4.53, 4.46]
G = 0.174
x_sred = 4.522
##p = lambda x: (1 / (G(2 * pi) ** 0.5)) * np.exp(-1 * ((x - x_sred) ** 2 / (2 * G ** 2)))
##l_p = []
##for i in massy:
##    l_p.append(i)
# plt.hist(massy, 5, label='гистограмма')
plt.title(label='Распределение масс грузиков', loc='center', fontweight='regular')
##plt.plot(massy, l_p)
ax.grid()
ax.set_xlabel('Масса, г')
sns_plot = sns.distplot(massy, hist=True, kde=True,
                        bins=5, color='red', label='реальное распределение')
plt.legend()
plt.show()
