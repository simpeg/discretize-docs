import discretize
import numpy as np
import matplotlib.pyplot as plt
locs = np.random.rand(50)*0.8+0.1
x = np.linspace(0, 1, 7)
dense = np.linspace(0, 1, 200)
fun = lambda x: np.cos(2*np.pi*x)
Q = discretize.utils.interpmat(locs, x)
plt.plot(x, fun(x), 'bs-')
plt.plot(dense, fun(dense), 'y:')
plt.plot(locs, Q*fun(x), 'mo')
plt.plot(locs, fun(locs), 'rx')
plt.show()