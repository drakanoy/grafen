import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

fig = plt.figure(figsize=(40, 9))
ax_3d = fig.add_subplot(projection='3d')
ax_3d.set_xlim([0, 100])  # Задание пределов оси X
ax_3d.set_ylim([0, 100])  # Задание пределов оси Y
ax_3d.set_zlim([-2, 2])

#  x = np.arange(-10*np.pi, 10*np.pi, 0.5)  # старые координаты
#  y = np.arange(-10*np.pi, 10*np.pi, 0.5)  # старые координаты
x = np.arange(0, 100, 0.5)
y = np.arange(0, 100, 0.5)
separation = 20.0  # Расстояние между центрами окружностей в см
side = 100.0  # Сторона квадрата в см
# Вычисляем позиции источников
x1 = side / 2 - 40
y1 = side / 2 + separation / 2
x2 = side / 2 - 40
y2 = side / 2 - separation / 2
xgrig, ygrid = np.meshgrid(x, y)

phasa = np.arange(0, 2*np.pi, 0.1)
frames = []
w = 1

for p in phasa:
    # с затуханием
    zgrig = np.cos(w*p-np.sqrt((xgrig - x1) ** 2 + (ygrid - y1) ** 2)) / np.sqrt((xgrig - x1) ** 2 + (ygrid - y1) ** 2)**0.5 + np.cos(w*p-np.sqrt((xgrig - x2) ** 2 + (ygrid - y2) ** 2)) / np.sqrt((xgrig - x2) ** 2 + (ygrid - y2) ** 2)**0.5
    # без затухания
    #zgrig = np.cos(w * p - np.sqrt((xgrig - x1) ** 2 + (ygrid - y1) ** 2)) + np.cos(w * p - np.sqrt((xgrig - x2) ** 2 + (ygrid - y2) ** 2))

    line = ax_3d.plot_surface(xgrig, ygrid, zgrig, cmap='plasma')
    frames.append([line])


animation = ArtistAnimation(
    fig,           # Фигура, где отображается анимация
    frames,        # Кадры
    interval=30,   # Задержка между кадрами в мс
    blit=True,     # Использовать ли двойную буферизацию
    repeat=True    # Зациклить ли анимацию
)
#plt.colorbar()
plt.show()
