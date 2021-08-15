import numpy as np
import matplotlib.pyplot as plt


e = 0
t = 2
d = 10 ** -8
y = lambda x: e + 2 * t * np.cos(x * d)
fig = plt.subplots()
x = np.linspace(-10**8, 10**8, 1000000)
plt.plot(x, y(x))
plt.show()