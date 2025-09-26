import numpy as np
from math import pi
import matplotlib.pyplot as plt

def mu(Eg, T):
    return - Eg/2 + 3*np.log(3)/4 * T

def n(Eg, T):
    return 2*(T)**(3/2)*np.exp(-Eg/T)

fig, ax = plt.subplots()
T = np.linspace(0, 1, 10000)
y = mu(1, T)
y_1 = n(1, T)
plt.plot(T, y_1, '-r', label='$n$ и $p$')
plt.title(label='$n$ и $p$', loc='center', fontweight='regular')
ax.grid()
ax.set_xlabel('$kT$ $(eV)$')
ax.set_ylabel('$n$ и $p$ $(cm^{-3})$')
plt.legend()
plt.show()