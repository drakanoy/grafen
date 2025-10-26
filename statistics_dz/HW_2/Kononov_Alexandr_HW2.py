import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, t, chi2

data = np.loadtxt('5.dat')
n = len(data)
x, y, sigma = data.T

# Строим график
fig, ax = plt.subplots()
plt.errorbar(x, y, yerr=sigma, fmt='o', capsize=4, label='Экспериментальные данные')
ax.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.title(label='График точек с погрешностями', loc='center', fontweight='regular')
plt.legend()
plt.show()

def r(x, A, B, w):
    return A*np.sin(w*x) + B*np.cos(w*x)

def x2(x, y, sigma, r, A, B, w):
    n = len(x)
    f = 0
    for i in range(n):
        f += ( (y[i]-r(x[i], A, B, w))/sigma[i] )**2
    return f

def Jacobian(x, A, B, w):
    """J_{i,:} = [∂m/∂A, ∂m/∂B, ∂m/∂w] в точке x_i."""
    S = np.sin(w*x)
    C = np.cos(w*x)
    J = np.zeros((x.size, 3), dtype=float)
    J[:, 0] = S                          # ∂m/∂A
    J[:, 1] = C                          # ∂m/∂B
    J[:, 2] = A * x * C - B * x * S      # ∂m/∂w
    return J

def Hessian(x, A, B, w):
    n = len(x)
    S = np.sin(w * x)
    C = np.cos(w * x)
    H = np.zeros((n, 3, 3), dtype=float)

    H[:, 0, 2] = x * C  # ∂2r/∂A∂w
    H[:, 2, 0] = H[:, 0, 2]  # симметрия

    H[:, 1, 2] = -x * S  # ∂2r/∂B∂w
    H[:, 2, 1] = H[:, 1, 2]  # симметрия

    H[:, 2, 2] = -A * (x ** 2) * S - B * (x ** 2) * C  # ∂2r/∂w^2
    return H

def d_and_D(x, y, sigma, A, B, w, r, J):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    sigma = np.asarray(sigma, float)

    r = r(x, A, B, w)
    J = J(x, A, B, w)

    # d_k = sum (y - r)/σ^2 * ∂r/∂a_k
    d = sum(J * ((y - r) / (sigma ** 2))[:, None])

    # D_kl = sum 1/σ^2 [ ∂r/∂a_k ∂r/∂a_l - (y-r) * ∂²r/∂a_k∂a_l ]
    D = J.T @ (J / (sigma ** 2)[:, None])

    return d, D

A = 0.9
B = 0.9
w = 0.9
x2_0 = x2(x, y, sigma, r, A, B, w)
lamda = 0.001
dx2 = np.inf
while abs(dx2) >= 10**(-6):
    d, D = d_and_D(x, y, sigma, A, B, w, r, Jacobian)
    diag_idx = np.diag_indices_from(D)
    D[diag_idx] *= (1.0 + lamda)

    # решаем систему D' δa = d
    delta = np.linalg.solve(D, d)
    A_new, B_new, w_new = A + delta[0], B + delta[1], w + delta[2]
    x2_new = x2(x, y, sigma, r, A_new, B_new, w_new)
    if x2_new >= x2_0:
        lamda *= 10
    else:
        dx2 = x2_0 - x2_new
        A, B, w, x2_0 = A_new, B_new, w_new, x2_new
        lamda /= 10
        C = np.linalg.inv(D)


print(f"A = {A:.2f} +- {C[0][0]**0.5:.2f}")
print(f"B = {B:.2f} +- {C[1][1]**0.5:.2f}")
print(f"w = {w:.3f} +- {C[2][2]**0.5:.3f}")
print('матрица ковариаций')
print(C)

print('согласуется ли модель по критерию х2 в доверительном интервале 1 − a = 0.683? (1sigma критерий n -> +00):', (n-3) - (2*(n-3))**0.5 < x2_0 < (n-3) + (2*(n-3))**0.5)
a = 1 - 0.683
print('согласуется ли модель по критерию х2 в доверительном интервале 1 − a = 0.683? (1sigma честное x2):', chi2.ppf(a/2, n-3) < x2_0 < chi2.ppf(1-a/2, n-3))
a = 1 - 0.954
print('согласуется ли модель по критерию х2 в доверительном интервале 1 − a = 0.954? (2sigma честное x2):', chi2.ppf(a/2, n-3) < x2_0 < chi2.ppf(1-a/2, n-3))

fig, ax = plt.subplots()
plt.errorbar(x, y, yerr=sigma, fmt='o', capsize=4, label='Экспериментальные данные')
x = np.linspace(-20, 10, 1000)
y = r(x, A, B, w)
plt.plot(x, y, '-r', label='МНК')
ax.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.title(label='График точек с погрешностями и МКН', loc='center', fontweight='regular')
plt.legend()
plt.show()
