import numpy as np
import matplotlib.pyplot as plt

w1=2.0
w2=1.0
γ1=0.32
γ2=0.1
g=0.5
f1=1.0
f2=0

omega=np.linspace(0.5,3,400)

x1_real = np.zeros_like(omega)
x1_imag = np.zeros_like(omega)
x1_abs = np.zeros_like(omega)

for i,w in enumerate(omega):
  matrix=np.array([
      [w1 - w - 1j*γ1, g],
      [g, w2 - w -1j*γ2]
  ])
  f = 1j*np.array([f1,f2])
  x = np.linalg.solve(matrix,f)
  x1_real[i] = x[0].real
  x1_imag[i] = x[0].imag
  x1_abs = np.abs(x[0])**2


plt.plot(omega,x1_real)
plt.plot(omega,x1_imag)
plt.legend()
plt.grid(True)
plt.show()
