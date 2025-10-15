import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


def edf(data, a):# выборочная функция распределения и ее погрешность и IQR
    data.sort()
    n = len(data)
    y = np.arange(1, n + 1) / n
    e = (1/(2*n) * np.log(2/a))**0.5
    k_075 = np.ceil(0.75 * n).astype(int)
    k_075 = np.clip(k_075, 1, n) # квантиль 0.75

    k_025 = np.ceil(0.25 * n).astype(int)
    k_025 = np.clip(k_025, 1, n) # квантиль 0.25
    IQR = k_075 - k_025
    return y, e, IQR

def kde(x, data, s2_kernel, h):
    n = len(data)
    f = 1/n * sum(1/h * norm.pdf((x - data)/h, scale=(s2_kernel)**0.5))
    return f


data = np.loadtxt('5.dat') # выборка
n = len(data) # длина выборки

mu = 1/(n) * sum(data) # выборочное среднее
s2 = 1/(n - 1) * sum((data - mu)**2) # выборочная дисперсия

s2_m = s2/n # дисперсия выборочного среднего
mu4 = 1/(n) * sum((data - mu)**4) # центральный 4 момент
D_s2m = 1/(n)**3 * (mu4 + (n-3)/(n-1)*s2**2) # дисперсия дисперсии выборочного среднего

# у нас уровень значимости 1-а = 90% ==> надо искать квантиль z_0.05
a = 1 - 0.9
z = norm.ppf(1 - a/2)

print(f'выборочное среднее на уровне доверия 90%: {mu:.1f} ± {z*(s2_m)**0.5:.1f}')
print(f'выборочная дисперсия на уровне доверия 90%: {s2:.1f} ± {z*(D_s2m)**0.5:.1f}')

# выборочная функция распр
y, e, IQR = edf(data, a)

# строим графики

fig, ax = plt.subplots()
plt.plot(data, y, '-b', label='edf')
plt.plot(data, y+e, '-r', label='edf+e')
plt.plot(data, y-e, '-r', label='edf-e')

plt.title(label='Выборочная функция распределения', loc='center', fontweight='regular')
ax.grid()
ax.set_xlabel('$x$')
ax.set_ylabel('$F_n$')
plt.legend()
plt.show()

# гистограмма
fig, ax = plt.subplots()
h = 2 * IQR/ n**(1/3) # оптимальная ширина бина
nbins = int(np.ceil((max(data) - min(data)) / h)) # число бинов
edges = np.linspace(min(data), max(data), nbins + 1)

ax.hist(data, bins=edges, density=True, edgecolor='black', alpha=0.7, label='Гистограмма нормарованная')
ax.grid()
ax.set_xlabel('$x$')
ax.set_ylabel('$f_n$')
plt.title(label='Гистограмма', loc='center', fontweight='regular')
plt.legend()
plt.show()

# kde
fig, ax = plt.subplots()
sigma = min((s2_m)**0.5, IQR/1.34)
h = 1.06 * sigma/ n**(1/5) # оптимальная ширина бина
x = np.linspace(0, 110, 1000)

plt.plot(x, [kde(i, data, s2, h) for i in x], '-b', label='kde')
ax.grid()
ax.set_xlabel('$x$')
ax.set_ylabel('$f_n$')
plt.title(label='kde', loc='center', fontweight='regular')
plt.legend()
plt.show()


# гистограмма и kde
fig, ax = plt.subplots()
h_1 = 2 * IQR/ n**(1/3) # оптимальная ширина бина для гистограммы
nbins = int(np.ceil((max(data) - min(data)) / h_1)) # число бинов
edges = np.linspace(min(data), max(data), nbins + 1)

x = np.linspace(0, 110, 1000)
ax.hist(data, bins=edges, density=True, edgecolor='black', alpha=0.7, label='Гистограмма нормарованная')


sigma = min((s2_m)**0.5, IQR/1.34)
h_2 = 1.06 * sigma/ n**(1/5) # оптимальная ширина бина для kde
#x = np.linspace(0, 110, 1000)
plt.plot(x, [kde(i, data, s2, h_2) for i in x], '-b', label='kde')

ax.grid()
ax.set_xlabel('$x$')
ax.set_ylabel('$f_n$')
plt.title(label='Гистограмма и kde', loc='center', fontweight='regular')
plt.legend()
plt.show()