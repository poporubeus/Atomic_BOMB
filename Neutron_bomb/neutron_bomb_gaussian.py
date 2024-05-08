import numpy as np
from scipy.integrate import dblquad
import matplotlib.pyplot as plt
from matplotlib import cm


L = 15.7


def function(x: np.array, y: np.array) -> float:
    t = L/4
    return ((1-(x/L))*(1-(y/L))*x*y) / t**2


def integrand(x: np.array, y: np.array, p: int, q: int) -> float:
    u = 4/(L**2)
    return u*function(x, y)*np.sin(p*np.pi*x/L)*np.sin(q*np.pi*y/L)


def Integrate(f: callable) -> np.array:
    N = 5
    a_pq_coeffs = np.zeros(shape=(N, N))
    for p in range(N):
        for q in range(N):
            integral, _ = dblquad(f, 0, L, lambda x: 0, lambda x: L, args=(p, q))
            a_pq_coeffs[p, q] = integral
    return a_pq_coeffs


result = Integrate(f=integrand)


def n_distribution(apq: np.array, x: np.array, y: np.array) -> float:
    eta = 1.8958e8
    mu = 2.3446e5
    t = 1e-7
    N = 5
    n = 0
    for i in range(N):
        for j in range(N):
            n += apq[i, j]*np.exp(eta*t-mu*((i*np.pi/L)**2 +
                                            (j*np.pi/L)**2)*t)*np.sin(i*np.pi*x/L)*np.sin(j*np.pi*y/L)
    return n


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
X = np.arange(0, L, 0.1)
Y = np.arange(0, L, 0.1)
X, Y = np.meshgrid(X, Y)
n_gaussian = n_distribution(result, X, Y)
Z = n_gaussian

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()