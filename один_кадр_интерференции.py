import numpy as np
from pylab import imshow, gray, show
import matplotlib.pyplot as plt

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
for t in np.arange(0, 2 * np.pi, 0.1):
    # Создаем массив для хранения высот
    xi = np.empty([points, points], float)
    # Вычисляем значения в массиве
    for i in range(points):
        y = spacing * i
        for j in range(points):
            x = spacing * j
            r1 = np.sqrt((x - x1) ** 2 + (y - y1) ** 2)
            r2 = np.sqrt((x - x2) ** 2 + (y - y2) ** 2)
            xi[i, j] = (xi0 * np.sin(w * t - k * r1) + xi0 * np.sin(w * t - k * r2))**2
    frames.append(xi)

# Отображение одного кадра (например, первого кадра)
print(len(frames))
a = frames[0]
for i in range(1, 63):
    a += frames[i]
print(a/500)
y_list = []
for i in range(len(a)):
    y_list.append(a[i][375])
print(y_list)
plt.imshow(frames[0], cmap='plasma', origin="lower", extent=[0, 1*side, 0, 1*side])
plt.xticks(np.arange(0, 1*side, 10))
plt.yticks(np.arange(0, 1*side, 10))
plt.colorbar()
plt.grid()
plt.show()
plt.plot(list(range(500)), y_list, 'r')
plt.grid()
plt.show()
