import numpy as np
import pandas as pd
import corner
import matplotlib.pyplot as plt



data = np.loadtxt('5.dat')
n = len(data)
x, y, s_obs = data.T
alpha = 0.05
a0, b0 = 1.0, 1.0
tau = 5.0
w_min, w_max = 0.05, 5.0
rng = np.random.default_rng()

# модель A*np.sin(w*x) + B*np.cos(w*x)
def r(w):
    return np.column_stack([np.sin(w*x), np.cos(w*x)])


# Приоры
w = rng.uniform(w_min, w_max)                 # приор для w
beta = rng.normal(loc=0.0, scale=tau, size=2) # A ~ N(0, tau**2)    B ~ N(0, tau**2) beta = (A, B)
sigma2 = 1.0 / rng.gamma(shape=a0, scale=1.0/b0)  # 1/ Gamma(a0,b0)


# Монте-Карло

def loglik(w, beta, sigma2):
    X = r(w)
    resid = y - X @ beta
    return -0.5*np.sum(
        np.log(2*np.pi*sigma2*(s_obs**2)) + (resid**2)/(sigma2*(s_obs**2))
    )

def sample_beta(w, sigma2):
    X = r(w)
    X_t = X / s_obs[:, None]
    y_t = y / s_obs

    Prec = (X_t.T @ X_t) / sigma2 + np.eye(2) / (tau**2)
    Cov = np.linalg.inv(Prec)
    mu = Cov @ ((X_t.T @ y_t) / sigma2)

    L = np.linalg.cholesky(Cov)
    return mu + L @ rng.normal(size=2)

def sample_sigma2(w, beta):
    X = r(w)
    resid = y - X @ beta
    S = float(np.sum((resid / s_obs) ** 2))
    a = a0 + n/2
    b = b0 + 0.5*S
    return 1.0 / rng.gamma(shape=a, scale=1.0/b)

# страрт цепи

n_iter = 30000
burn = 6000
thin = 6
prop_sd = 0.05

samples = []
acc = 0

for t in range(n_iter):
    beta = sample_beta(w, sigma2)
    sigma2 = sample_sigma2(w, beta)

    w_prop = w + rng.normal(scale=prop_sd)

    if w_min <= w_prop <= w_max:
        lp_cur = loglik(w, beta, sigma2)
        lp_prop = loglik(w_prop, beta, sigma2)

        if np.log(rng.uniform()) < (lp_prop - lp_cur):
            w = w_prop
            acc += 1

    if t >= burn and ((t - burn) % thin == 0):
        samples.append([beta[0], beta[1], w, np.sqrt(sigma2)])

samples1 = []
for i in samples:
    spisok = []
    for j in range(3):
        spisok.append(i[j])
    samples1.append(spisok)


samples1 = np.array(samples1)
samples = np.array(samples)

# Интервалы
df = pd.DataFrame(samples)
print('A', df[0].mean(), 'доверительный интервал при alpha=0.05: (', df[0].quantile(alpha/2), ',', df[0].quantile(1-alpha/2), ')')
print('B', df[1].mean(), 'доверительный интервал при alpha=0.05: (', df[1].quantile(alpha/2), ',', df[1].quantile(1-alpha/2), ')')
print('w', df[2].mean(), 'доверительный интервал при alpha=0.05: (', df[2].quantile(alpha/2), ',', df[2].quantile(1-alpha/2), ')')


print('из задания 2:')
print('A = -0.35 +- 0.06')
print('B = -0.99 +- 0.05')
print('w = 0.703 +- 0.006')

fig = corner.corner(
    samples1,
    labels=["A", "B", "w"],
    quantiles=[0.025, 0.5, 0.975],
    show_titles=True,
    title_fmt=".4f",
)
plt.show()
