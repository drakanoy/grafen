import numpy as np
from pylab import imshow, gray, show
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

wavelength = 5  # длина волны
w = 5  # частота
k = 2 * np.pi / wavelength
xi0 = 1.0
separation = 20.0  # Расстояние между центрами окружностей в см
side = 100.0  # Сторона квадрата в см
points = 500  # Количество точек сетки по каждой стороне
spacing = side / points  # Шаг точек в см

# Вычисляем позиции источников
x1 = side / 2 - 40
y1 = side / 2 + separation / 2
x2 = side / 2 - 40
y2 = side / 2 - separation / 2

frames = []  # кадры
fig = plt.figure(figsize=(40, 9))
ax = fig.add_subplot()
cax = fig.add_axes([0.9, 0.15, 0.02, 0.7])
for t in np.arange(0, 2*np.pi, 0.1):
    # Создаем массив для хранения высот
    xi = np.empty([points, points], float)
    # Вычисляем значения в массиве
    for i in range(points):
        y = spacing * i
        for j in range(points):
            x = spacing * j
            r1 = np.sqrt((x - x1) ** 2 + (y - y1) ** 2)
            r2 = np.sqrt((x - x2) ** 2 + (y - y2) ** 2)
            xi[i, j] = xi0 * np.sin(w * t - k * r1) + xi0 * np.sin(w * t - k * r2)
    im = ax.imshow(xi, cmap='plasma', origin="lower", extent=[0, side, 0, side])
    frames.append([im])


#imshow(xi, cmap='plasma', origin="lower", extent=[0, side, 0, side])
#show()
animation = ArtistAnimation(
    fig,           # Фигура, где отображается анимация
    frames,        # Кадры
    interval=30,   # Задержка между кадрами в мс
    blit=True,     # Использовать ли двойную буферизацию
    repeat=True,    # Зациклить ли анимацию
#    cmap='plasma'
)
#plt.colorbar()
fig.colorbar(im, cax=cax)
plt.show()
