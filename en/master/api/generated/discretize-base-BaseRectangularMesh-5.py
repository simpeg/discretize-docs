# Plot a slice of a 3D ``TensorMesh`` solution to a Laplace's equaiton.

# First build the mesh:

from matplotlib import pyplot as plt
import discretize
from pymatsolver import Solver
import numpy as np
hx = [(5, 2, -1.3), (2, 4), (5, 2, 1.3)]
hy = [(2, 2, -1.3), (2, 6), (2, 2, 1.3)]
hz = [(2, 2, -1.3), (2, 6), (2, 2, 1.3)]
M = discretize.TensorMesh([hx, hy, hz])

# then build the necessary parts of the PDE:

q = np.zeros(M.vnC)
q[[4, 4], [4, 4], [2, 6]]=[-1, 1]
q = discretize.utils.mkvc(q)
A = M.face_divergence * M.cell_gradient
b = Solver(A) * (q)

# and finaly, plot the vector values of the result, which are defined on faces

M.plot_slice(M.cell_gradient*b, 'F', view='vec', grid=True, pcolor_opts={'alpha':0.8})
plt.show()
