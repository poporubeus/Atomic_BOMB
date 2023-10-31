import numpy as np
import matplotlib.pyplot as plt

mu = 2.3446e5
eta= 1.8958e8
N = 100
r1 = 0.115

### replace the path with your location where you saved the codes
with open('/Users/francescoaldoventurelli/Desktop/Neutron_bomb/Integral_results', 'r') as f:
    Integralvalues = [line.strip() for line in f]
Integralvalues = [float(x) for x in Integralvalues]


def n_spherical(r, t):
  n = 0
  for i in range(N):
    n += (Integralvalues[i]/r)*np.exp(eta*t-mu*((i)*np.pi/r1)**2*t)*np.sin((i)*np.pi*r/r1)
  return n

r = np.linspace(-r1,r1,100)
t = np.linspace(0,2e-06,100)
R,T = np.meshgrid(r,t)

figure = plt.figure(figsize=(15,8))
ax = plt.axes(projection='3d')
ax.plot_surface(R, T, n_spherical(R, T),cmap='magma')

ax.set_xlabel('r [mt]')
ax.set_ylabel('t [sec]')
ax.set_zlabel('n(r,t)')
plt.title("Neutron diffusion during time with Dirichlet conditions")
plt.savefig("/Users/francescoaldoventurelli/Desktop/Neutron_bomb/Dirchlet_BOMB.jpg")
plt.show()