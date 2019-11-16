import numpy as np
import scipy.special
import matplotlib.pyplot as plt


def norm(n):
    N2 = 2**n * np.math.factorial(n) * np.sqrt(np.pi)
    return np.sqrt(N2)


x = np.linspace(-5, 5, 256)
ep = np.exp(-0.5*x*x)
hmq0 = scipy.special.eval_hermite(0, x)*ep/norm(0)
hmq1 = scipy.special.eval_hermite(1, x)*ep/norm(1)
hmq2 = scipy.special.eval_hermite(2, x)*ep/norm(2)
hmq3 = scipy.special.eval_hermite(3, x)*ep/norm(3)

fig, ax = plt.subplots(1, 1)

ax.plot(x, hmq0, label='0')
ax.plot(x, hmq1, label='1')
ax.plot(x, hmq2, label='2')
ax.plot(x, hmq3, label='3')
ax.axhline(color="grey", zorder=-1, lw=0.5)
ax.axvline(color="grey", zorder=-1, lw=0.5)
ax.set_title('Hermite')
ax.set_xlim(-5, 5)
ax.legend(loc='upper left')

plt.savefig('hermite.pdf')
plt.show()
