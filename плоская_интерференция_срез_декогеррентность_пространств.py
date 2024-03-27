import numpy as np
from pylab import imshow, gray, show
import matplotlib.pyplot as plt

wavelength = 2  # длина волны в м
k = 2 * np.pi / wavelength
w0 = 1  # 3 * 10**8 / (2*np.pi * wavelength) # частота в рад/с
dw = 0.1
xi0 = 1.0
separation = 20.0  # Расстояние между центрами окружностей в м
side = 100.0  # Сторона квадрата в м
points = 500  # Количество точек сетки по каждой стороне
spacing = side / points  # Шаг точек в м

# Вычисляем позиции источников
x1 = side / 2 - 40
y1 = side / 2 + separation / 2
x2 = side / 2 - 40
y2 = side / 2 - separation / 2

frames = []  # кадры
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
            xi[i, j] = 0
            # Вычисление высоты с учетом декогерентности
            for w in np.arange(w0-dw, w0+dw, 0.01):
                xi[i, j] += (xi0 * np.sin(w * t - k * r1) + xi0 * np.sin(w * t - k * r2))**2 / 20
    frames.append(xi)

# Отображение одного кадра (например, первого кадра)
dlina = len(frames)
a = frames[0]
for i in range(1, dlina):
    a += frames[i]
a = a / dlina
print(a)
y_list = []
for i in range(len(a)):
    y_list.append(a[i][375])
print(y_list)
plt.imshow(frames[0] / dlina, cmap='plasma', origin="lower", extent=[0, 1*side, 0, 1*side])
plt.xticks(np.arange(0, 1*side, 10))
plt.yticks(np.arange(0, 1*side, 10))
plt.colorbar()
plt.grid()
plt.show()
x_list = [i / 5 for i in range(500)]
plt.plot(x_list, y_list, 'r', label='model')
x_list = [i / 5 for i in range(500)]
x_listk = [(i / 5 - 50) * separation / 65 * k for i in range(500)]
plt.plot(x_list, 1 + np.cos(x_listk), label='teor')
plt.legend()
plt.grid()
plt.show()
x_list = [i / 5 for i in range(500)]
plt.plot(x_list, y_list, 'r', label='model')
plt.legend()
plt.grid()
plt.show()