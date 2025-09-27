import math
import numpy as np
import matplotlib.pyplot as plt

# ---------- Adaptive Simpson ----------
def _simpson(f, a, b):
    c = (a + b) / 2.0
    h = b - a
    return (h/6.0) * (f(a) + 4.0 * f(c) + f(b))

def _adaptive_simpson(f, a, b, eps=1e-8, maxdepth=20):
    fa, fb, fc = f(a), f(b), f((a+b)/2.0)
    S = _simpson(f, a, b)
    def rec(a,b,eps,S,fa,fb,fc,depth):
        c = (a+b)/2.0
        ld = (a+c)/2.0
        re = (c+b)/2.0
        fd = f(ld); fe = f(re)
        Sleft  = (c-a)/6.0 * (fa + 4.0*fd + fc)
        Sright = (b-c)/6.0 * (fc + 4.0*fe + fb)
        if depth<=0 or abs(Sleft+Sright-S) < 15*eps:
            return Sleft + Sright + (Sleft+Sright-S)/15.0
        return rec(a,c,eps/2,Sleft,fa,fc,fd,depth-1) + rec(c,b,eps/2,Sright,fc,fb,fe,depth-1)
    return rec(a,b,eps,S,fa,fb,fc,maxdepth)

# ---------- F_{-1/2}(eta) via x = u^2 ----------
def F_mhalf(eta):
    # ∫_0^∞ x^{-1/2}/(1+e^{x-η}) dx = 2∫_0^∞ du /(1+e^{u^2-η})
    def g(u):
        return 2.0 / (1.0 + math.exp(u*u - eta))
    xmax = max(eta + 20.0, 50.0)
    umax = math.sqrt(xmax)
    return _adaptive_simpson(g, 0.0, umax, eps=1e-8, maxdepth=18)

# ---------- Inversion for η from y = n / T^(1/2) ----------
def eta_from_y(y, tol=1e-9, maxiter=200):
    lo, hi = -40.0, 60.0
    f_lo = F_mhalf(lo) - y
    f_hi = F_mhalf(hi) - y
    k=0
    while f_lo > 0 and k<5:
        hi = lo; f_hi = f_lo
        lo -= 20; f_lo = F_mhalf(lo) - y; k+=1
    k=0
    while f_hi < 0 and k<5:
        lo = hi; f_lo = f_hi
        hi += 20; f_hi = F_mhalf(hi) - y; k+=1
    for _ in range(maxiter):
        mid = 0.5*(lo+hi)
        f_mid = F_mhalf(mid) - y
        if abs(f_mid) < tol or (hi-lo) < 1e-10:
            return mid
        if f_mid > 0:
            hi = mid
        else:
            lo = mid
    return 0.5*(lo+hi)

# ---------- Asymptotics ----------
def mu_degenerate(T, n):
    E_F = (n/2.0)**2
    return E_F * (1.0 + (math.pi**2/12.0) * (T/E_F)**2)

def mu_classical(T, n):
    return T * (math.log(n) - 0.5*math.log(T) - 0.5*math.log(math.pi))

# ---------- Main plotting ----------
def plot_mu_vs_T(n=1.0, T_min=1e-3, T_max=3.0, N=140):
    Ts = np.geomspace(T_min, T_max, N)
    mu_num = []
    mu_deg = []
    mu_cl  = []
    for T in Ts:
        y = n / (T**0.5)
        eta = eta_from_y(y)
        mu_num.append(eta*T)
        mu_deg.append(mu_degenerate(T, n))
        mu_cl.append(mu_classical(T, n))
    mu_num = np.array(mu_num)
    mu_deg = np.array(mu_deg)
    mu_cl  = np.array(mu_cl)

    plt.figure(figsize=(7,5))
    plt.plot(Ts, mu_num, label="μ(T) численно")
    plt.plot(Ts, mu_deg, linestyle="--", label="kT≪Ef")
    plt.plot(Ts, mu_cl,  linestyle=":",  label="kT≫Ef")
    plt.xlabel("kT")
    plt.ylabel("μ")
    plt.title("μ(T) 1D")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_mu_vs_T(n=1.0, T_min=1e-3, T_max=3.0, N=140)
