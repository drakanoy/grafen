import numpy as np
import matplotlib.pyplot as plt
from math import pi

t1 = 2
t2 = 1
d = 10 ** -8
y = lambda x: (t1 ** 2 + t2 ** 2 + 2 * t1 * t2 * np.cos(x * d)) ** 0.5
y1 = lambda x: -((t1 ** 2 + t2 ** 2 + 2 * t1 * t2 * np.cos(x * d)) ** 0.5)
fig, ax = plt.subplots()
x = np.linspace(-2 * pi / d, 2 * pi / d, 10000)
plt.plot(x / 10 ** 8, y(x))
plt.plot(x / 10 ** 8, y1(x))
ax.grid()
ax.set_xlabel('Wave vector (k), $10^8$')
ax.set_ylabel('Energy (E)')
plt.show()
