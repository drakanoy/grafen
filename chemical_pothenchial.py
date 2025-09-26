import numpy as np
from math import pi
import matplotlib.pyplot as plt

def mu(Eg, T):
    return - Eg/2 + 3*np.log(3)/4 * T

fig, ax = plt.subplots()
x = np.linspace(0, 1, 10000)
y = mu(1, x)
plt.plot(x, y, '-r', label='$\\mu$ при $E_g = 1 eV$')
plt.title(label='$\\mu$ при $E_g = 1 eV$', loc='center', fontweight='regular')
ax.grid()
ax.set_xlabel('$kT$ $s(eV)$')
ax.set_ylabel('$\\mu$ $(eV)$')
plt.legend()
plt.show()