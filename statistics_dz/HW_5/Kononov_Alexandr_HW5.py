import numpy as np
import pandas as pd



data = np.loadtxt('5.dat')
n = len(data)
x, y, s_obs = data.T
alpha = 0.05

# модель A*np.sin(w*x) + B*np.cos(w*x)

# Приоры
# быстрый поиск по сетке для w0
def fit_beta_w(w, tau2_ridge=1e12):
    X = np.column_stack([np.sin(w*x), np.cos(w*x)])
    X_t = X / s_obs[:, None]
    y_t = y / s_obs
    XtX = X_t.T @ X_t + np.eye(2) / tau2_ridge
    Xty = X_t.T @ y_t
    beta = np.linalg.solve(XtX, Xty)
    resid = y - X @ beta
    S = np.sum((resid / s_obs) ** 2)
    return beta, S


ws = np.linspace(0.05, 5.0, 4000)
Ss = np.array([fit_beta_w(w)[1] for w in ws])
w0 = float(ws[np.argmin(Ss)])

#приор для w
mu_logw = np.log(w0)
sd_logw = 1.0

def logprior_logw(logw):
    return -0.5*((logw-mu_logw)/sd_logw)**2 - np.log(sd_logw*np.sqrt(2*np.pi))
#приорs для A, B
a0, b0 = 1.0, 1.0
tau = 5.0
# A ~ N(0, tau**2)    B ~ N(0, tau**2)
# betta = (A, B)


# Монте-Карло
rng = np.random.default_rng()

def sample_beta(w, sigma2):
    X = np.column_stack([np.sin(w*x), np.cos(w*x)])
    X_t = X / s_obs[:, None]
    y_t = y / s_obs
    Prec = (X_t.T @ X_t) / sigma2 + np.eye(2) / tau**2
    Cov = np.linalg.inv(Prec)
    mu = Cov @ ((X_t.T @ y_t) / sigma2)
    L = np.linalg.cholesky(Cov)
    return mu + L @ rng.normal(size=2)

def loglik(w, beta, sigma2):
    X = np.column_stack([np.sin(w*x), np.cos(w*x)])
    resid = y - X @ beta
    return -0.5*np.sum(np.log(2*np.pi*sigma2*(s_obs**2)) + (resid**2)/(sigma2*(s_obs**2)))

def sample_sigma2(w, beta):
    X = np.column_stack([np.sin(w*x), np.cos(w*x)])
    resid = y - X @ beta
    S = float(np.sum((resid / s_obs) ** 2))
    a = a0 + n/2
    b = b0 + 0.5*S
    return 1.0 / rng.gamma(shape=a, scale=1.0/b)

# страрт цепи
w = w0
logw = np.log(w)
beta = sample_beta(w, 1.0)
sigma2 = sample_sigma2(w, beta)

n_iter = 30000
burn = 6000
thin = 6
prop_sd = 0.05

samples = []
acc = 0

for t in range(n_iter):
    beta = sample_beta(w, sigma2)
    sigma2 = sample_sigma2(w, beta)

    logw_prop = logw + rng.normal(scale=prop_sd)
    w_prop = np.exp(logw_prop)

    lp_cur = loglik(w, beta, sigma2) + logprior_logw(logw)
    lp_prop = loglik(w_prop, beta, sigma2) + logprior_logw(logw_prop)

    if np.log(rng.uniform()) < (lp_prop - lp_cur):
        logw = logw_prop
        w = w_prop
        acc += 1

    if t >= burn and ((t - burn) % thin == 0):
        samples.append([beta[0], beta[1], w, np.sqrt(sigma2)])

samples = np.array(samples)
acc_rate = acc / n_iter

# Интервалы
df = pd.DataFrame(samples)
print('A', df[0].mean(), 'доверительный интервал при alpha=0.05: (', df[0].quantile(alpha/2), ',', df[0].quantile(1-alpha/2), ')')
print('B', df[1].mean(), 'доверительный интервал при alpha=0.05: (', df[1].quantile(alpha/2), ',', df[1].quantile(1-alpha/2), ')')
print('w', df[2].mean(), 'доверительный интервал при alpha=0.05: (', df[2].quantile(alpha/2), ',', df[2].quantile(1-alpha/2), ')')


print('из задания 2:')
print('A = -0.35 +- 0.06')
print('B = -0.99 +- 0.05')
print('w = 0.703 +- 0.006')