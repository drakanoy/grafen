import numpy as np
import matplotlib.pyplot as plt
from math import pi

e = 0
t = 2
d = 10 ** -8
y = lambda x: np.arcsin((x ** 3 - 6 * x) / 4) / d
y1 = lambda x: x
y2 = lambda x: (x ** 3 - 6 * x) / 4
fig = plt.subplots()
x = np.linspace(-0.73, 0.73, 10000)
plt.plot(y(x), (x))
plt.show()
