# We first create a very simple 2D tensor mesh on the [0, 1] boundary:

import matplotlib.pyplot as plt
import scipy.sparse as sp
import discretize
mesh = discretize.TensorMesh([32, 32])

# Define the `alpha`, `beta`, and `gamma` parameters for a zero - Dirichlet
# condition on the boundary, this corresponds to setting:

alpha = 1.0
beta = 0.0
gamma = 0.0
A, b = mesh.cell_gradient_weak_form_robin(alpha, beta, gamma)

# We can then represent the operation of taking the weak form of the gradient of a
# function defined on cell centers with appropriate robin boundary conditions as:

V = sp.diags(mesh.cell_volumes)
D = mesh.face_divergence
phi = np.sin(np.pi * mesh.cell_centers[:, 0]) * np.sin(np.pi * mesh.cell_centers[:, 1])
phi_grad = (-D.T @ V + A) @ phi + b
