# Here, we construct a 4 cell by 4 cell tensor mesh. For our first example we
# consider isotropic physical properties; that is, the physical properties
# of each cell are defined a scalar value. We construct the edge inner product
# matrix and visualize it with a spy plot. We then use
# **get_edge_inner_product_deriv** to construct the function handle
# :math:`\mathbf{F}(\mathbf{u})` and plot the evaluation of this function on a spy
# plot.
#
from discretize import TensorMesh
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams.update({'font.size': 14})
np.random.seed(45)
mesh = TensorMesh([[(1, 4)], [(1, 4)]])
#
# Next we create a random isotropic model vector, and a random vector to multiply
# the derivative with (for illustration purposes).
#
m = np.random.rand(mesh.nC)  # physical property parameters
u = np.random.rand(mesh.nF)  # vector of shape (n_edges)
Me = mesh.get_edge_inner_product(m)
F = mesh.get_edge_inner_product_deriv(m)  # Function handle
dFdm_u = F(u)
#
# Plot inner product matrix and its derivative matrix
#
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_axes([0.05, 0.05, 0.3, 0.8])
ax1.spy(Me, ms=6)
ax1.set_title("Edge Inner Product Matrix (Isotropic)", fontsize=14, pad=5)
ax1.set_xlabel("Edge Index", fontsize=12)
ax1.set_ylabel("Edge Index", fontsize=12)
ax2 = fig.add_axes([0.43, 0.05, 0.17, 0.8])
ax2.spy(dFdm_u, ms=6)
ax2.set_title(
    "$u^T \, \dfrac{\partial M(m)}{\partial m}$ (Isotropic)",
    fontsize=14, pad=5
)
ax2.set_xlabel("Parameter Index", fontsize=12)
ax2.set_ylabel("Edge Index", fontsize=12)
plt.show()
#
# For our second example, the physical properties on the mesh are fully
# anisotropic; that is, the physical properties of each cell are defined
# by a tensor with parameters :math:`\sigma_1`, :math:`\sigma_2` and :math:`\sigma_3`.
# Once again we construct the edge inner product matrix and visualize it with a
# spy plot. We then use **get_edge_inner_product_deriv** to construct the
# function handle :math:`\mathbf{F}(\mathbf{u})` and plot the evaluation
# of this function on a spy plot.
#
m = np.random.rand(mesh.nC, 3)  # physical property parameters
u = np.random.rand(mesh.nF)     # vector of shape (n_edges)
Me = mesh.get_edge_inner_product(m)
F = mesh.get_edge_inner_product_deriv(m)  # Function handle
dFdm_u = F(u)
#
# Plot the anisotropic inner product matrix and its derivative matrix
#
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_axes([0.05, 0.05, 0.3, 0.8])
ax1.spy(Me, ms=6)
ax1.set_title("Edge Inner Product (Full Tensor)", fontsize=14, pad=5)
ax1.set_xlabel("Edge Index", fontsize=12)
ax1.set_ylabel("Edge Index", fontsize=12)
ax2 = fig.add_axes([0.4, 0.05, 0.45, 0.8])
ax2.spy(dFdm_u, ms=6)
ax2.set_title(
    "$u^T \, \dfrac{\partial M(m)}{\partial m} \;$ (Full Tensor)",
    fontsize=14, pad=5
)
ax2.set_xlabel("Parameter Index", fontsize=12)
ax2.set_ylabel("Edge Index", fontsize=12)
plt.show()
