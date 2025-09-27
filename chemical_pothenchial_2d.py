import numpy as np
import matplotlib.pyplot as plt

def mu_exact(T, n):
    return T * np.log(np.expm1(n / T))

def mu_deg(T, n):
    # return n - T * np.exp(-n / T) # правильная формула с экспоненциальной поправкой
    return n + T*0

def mu_classical(T, n):
    return T * (np.log(n) - np.log(T))

def plot_mu_vs_T(n=1.0, T_min=0.01, T_max=10.0, N=200):
    Ts = np.geomspace(T_min, T_max, N)
    mu_ex = mu_exact(Ts, n)
    mu_lo = mu_deg(Ts, n)
    mu_hi = mu_classical(Ts, n)

    plt.figure(figsize=(7,5))
    plt.plot(Ts, mu_ex, label="μ(T) Численно")
    plt.plot(Ts, mu_lo, linestyle="--", label="kT≪Ef")
    plt.plot(Ts, mu_hi, linestyle=":", label="kT≫Ef")
    plt.xlabel("kT")
    plt.ylabel("μ")
    plt.title("μ(T) 2D")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_mu_vs_T()
