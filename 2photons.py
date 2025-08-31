import numpy as np
from math import pi
import matplotlib.pyplot as plt

def g2_1(delta, teta):
    return (2*delta**2 * np.cos(teta/2))**2 / (np.sin(teta/2)**2 + delta**2)**2
def g2_2(delta, teta, gamma):
    return (2* (1+delta**2) * gamma**2 * np.cos(teta/2)**2) / ((1+delta**2) * gamma**2 + np.sin(teta/2)**2 - delta*gamma * np.sin(teta))**2

fig, ax = plt.subplots()
x = np.linspace(0, 20, 10000)
y = g2_2(x, 2*pi, 1)
plt.plot(x, y, '-r', label='$g^{(2)}(0)$ при $\\theta = 2\pi$')
plt.title(label='$g^{(2)}(0)$ при $\\theta = 2\pi$', loc='center', fontweight='regular')
ax.grid()
ax.set_xlabel('$\\delta_N$')
ax.set_ylabel('$g^{(2)}(0)$')
plt.legend()
plt.show()