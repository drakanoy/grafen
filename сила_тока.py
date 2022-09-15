import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

x = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4]
y = [34, 137, 240, 355, 513, 604, 716, 836, 919, 985, 1036, 1084, 1109]
fig, ax = plt.subplots()
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
y1 = p(x)
plt.plot(x, y, '.', x, y1, '-r')
plt.title(label='Зависимость магнитной индукции от силы тока',loc='center',fontweight='regular')
ax.grid()
ax.set_xlabel('Сила тока, А')
ax.set_ylabel('Магнитная индукция, мТл')
plt.show()
