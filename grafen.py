import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

a = 10 ** -8
t = 1
E = lambda x, y: t * (1 + 4 * np.cos(x * a * 1.5) * np.cos(y * a * (3 ** 0.5) / 2) + 4 * np.cos(
    y * a * (3 ** 0.5) / 2) ** 2) ** 0.5
E1 = lambda x, y: -1 * t * (1 + 4 * np.cos(x * a * 1.5) * np.cos(y * a * (3 ** 0.5) / 2) + 4 * np.cos(
    y * a * (3 ** 0.5) / 2) ** 2) ** 0.5
fig = plt.figure(figsize=(10, 10))
ax_3d = fig.add_subplot(projection='3d')
x = np.arange(-1 * np.pi / (1.0 * a), 1 * np.pi / (1.0 * a), 100000)
y = np.arange(-1 * np.pi / (1.0 * a), 1 * np.pi / (1.0 * a), 100000)
xgrid, ygrid = np.meshgrid(x, y)
Egrid = E(xgrid, ygrid)
E1grid = E1(xgrid, ygrid)
ax_3d.plot_surface(xgrid / 10 ** 8, ygrid / 10 ** 8, Egrid, cmap='plasma')
ax_3d.plot_surface(xgrid / 10 ** 8, ygrid / 10 ** 8, E1grid, cmap=cm.viridis)
ax_3d.set_xlabel('Wave vector (kx), $10^8$')
ax_3d.set_ylabel('Wave vector (ky), $10^8$')
ax_3d.set_zlabel('Energy (E)')
plt.show()
# a = 10 ** -8
# t = 1
# E = lambda x, y: t * (1 + 4 * np.cos(x * a * 1.5) * np.cos(y * a * (3 ** 0.5) / 2) + 4 * np.cos(
# y * a * (3) ** 0.5 / 2) ** 2) ** 0.5

