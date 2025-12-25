import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, kstest, chi2, ks_2samp, gaussian_kde


data = np.loadtxt('5.dat')
n = len(data)
a = 0.05
b = 50000
s2 = np.var(data, ddof=1) # выборочная дисперсия

def bootstrap_percentile(data, b, a):
    rng = np.random.default_rng()
    idx = rng.integers(0, n, size=(b, n)) # список bootstrap выборок
    data_bootstrap = data[idx]
    s2_b = np.var(data_bootstrap, ddof=1, axis=1)
    z_a2, z_1_a2 = np.quantile(s2_b, [a / 2, 1 - a / 2]) # кванили
    return z_a2, z_1_a2

z_a2, z_1_a2 = bootstrap_percentile(data, b, a)
print('интервальная оценка на дисперсию bootstrap: (', z_a2, ',', z_1_a2, ')')
print('####################################################################################')


def jackknife(data):
    spisok_s2 = []
    for i in range(n):
        data_i = np.delete(data, i)
        spisok_s2.append(np.var(data_i, ddof=1))
    s2_jack = np.mean(spisok_s2)
    bias = (n - 1) * (s2_jack - s2)
    dispersia = 0
    for i in range(n):
        dispersia += (n-1)/n * (spisok_s2[i] - s2_jack)**2

    s2_min = s2 - bias - (dispersia)**0.5
    s2_max = s2 - bias + (dispersia) ** 0.5

    return bias, s2_min, s2_max

bias, s2_min, s2_max = jackknife(data)
print('bias дисперсии', bias)
print('интервальная оценка на дисперсию: (', s2_min, ',', s2_max, ')')
print('####################################################################################')



# стартовая точка
std = data.std(ddof=1)
q25, q75 = np.quantile(data, [0.25, 0.75])
iqr = q75 - q25
sigma = min(std, iqr/1.34)
h_0 = 0.9 * sigma * n ** (-1/5)
hs = h_0 * np.logspace(-1.0, 1.0, 20) # сетка


def crossvalidation(data, h):
    d = data[:, None] - data[None, :]
    d2 = d * d

    # первое слагаемое с квадратом kde
    term1 = np.exp(-d2 / (4 * h * h)).sum() * (1 / (n * n)) * (1 / (2 * np.sqrt(np.pi) * h))

    # второе слагаемое
    K = np.exp(-d2 / (2 * h * h))
    np.fill_diagonal(K, 0.0)  # исключаем i=j
    f_loo = K.sum(axis=1) * (1 / ((n - 1) * h * np.sqrt(2 * np.pi)))
    term2 = (2 / n) * f_loo.sum()

    return term1 - term2

scores = np.array([crossvalidation(data, h) for h in hs])
best_h = float(hs[np.argmin(scores)])
print(best_h, "лучшая ширина бина")
print('####################################################################################')


x = data[:int(n/2)]
y = data[int(n/2):]
T_obs = x.mean() - y.mean()
def permutation(x, y, b):
    rng = np.random.default_rng()
    z = np.concatenate([x, y])
    N = len(z)
    m = len(x)
    total = z.sum()
    Ts = []
    for i in range(b):
        idx = rng.permutation(N)[:m]
        sumX = z[idx].sum()
        sumY = total - sumX
        Ts.append((sumX/m) - (sumY/(N-m)))

    p_two = (np.sum(np.abs(Ts) >= abs(T_obs)) + 1) / (b + 1)
    return p_two

p = permutation(x, y, b)
print(p, 'p-value что две половины имеют одинковые распределения если судить по разности мат ожиданий')