import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, kstest, chi2, ks_2samp

data = np.loadtxt('5.dat')
n = len(data)
data_sorted = np.sort(data)

a = 0.05
Ka = 1.36
F = norm.cdf(data_sorted, loc=0, scale=1)
i = np.arange(1, n + 1)
D_plus  = np.max(i / n - F)
D_minus = np.max(F - (i - 1) / n)
Dn = max(D_plus, D_minus)


print((n)**0.5*Dn<=Ka, "Нет свидетельств против H0, по критерию Колмогорова")
p = kstest(data, 'norm', args=(0,1)).pvalue
print(p)
print(p>0.05, "критерий что p-value > alpha = 0.05")
print(p>0.1, "критерий что p-value > 0.1, и нет свидетельств против H0")

#############################################################################################
print('#############################################################################################')
# теперь проверка, что мат ожидание = 0 и дисперсия = 1

mu = 1/(n) * sum(data) # выборочное среднее
z_norm = norm.ppf(1 - a/2)  # квантиль норм распределения

print(-z_norm < (n)**0.5*mu < z_norm, 'Нет свидетельств против того, что мат ожидание = 0')
p = 2*(1-norm.cdf((n)**0.5*mu))
print(p)
print(p>0.05, "критерий что p-value > alpha = 0.05")
print(p>0.1, "критерий что p-value > 0.1, и нет свидетельств против H0")

#############################################################################################
print('#############################################################################################')

s2 = 1/(n - 1) * sum((data - mu)**2) # выборочная дисперсия
nu = n - 1  #  число степеней свободы
z_chi2_a_2 = chi2.ppf(a/2, nu)
z_chi2_1_a_2 = chi2.ppf(1-a/2, nu)

print(z_chi2_a_2 < (n-1)*s2 < z_chi2_1_a_2, 'отвергаем гипотезу Н0, что дисперсия = 0')
p = 2*min(chi2.cdf((n-1)*s2, nu), 1 - chi2.cdf((n-1)*s2, nu))
print(p)
print(p>0.05, "критерий что p-value > alpha = 0.05")
print(p>0.1, "критерий что p-value > 0.1, отвергаем гипотезу Н0, что дисперсия = 0")

#############################################################################################
print('#############################################################################################')

x = data[:int(n/2)]
y = data[int(n/2):]
xs = np.sort(x)
ys = np.sort(y)

nx = len(x)
ny = len(y)

xs = np.sort(x)
ys = np.sort(y)

i = 0
j = 0
Fn = 0.0
Gn = 0.0
D = 0.0

while i < nx or j < ny:
    if j >= ny or (i < nx and xs[i] < ys[j]):
        v = xs[i]
    elif i >= n or (j < ny and ys[j] < xs[i]):
        v = ys[j]
    else:
        v = xs[i]

    while i < nx and xs[i] == v:
        i += 1
    while j < ny and ys[j] == v:
        j += 1

    Fn = i / nx
    Gn = j / ny

    D = max(D, abs(Fn - Gn))
print((nx*ny/(nx+ny))**0.5*D<=Ka, "Нет свидетельств против H0, по критерию Смирнова")
p = ks_2samp(x, y).pvalue
print(p)
print(p>0.05, "критерий что p-value > alpha = 0.05")
print(p>0.1, "критерий что p-value > 0.1, и нет свидетельств против H0")