# Here we provide an example of edge inner product line matrix.
# For simplicity, we will work on a 2 x 2 x 2 tensor mesh.
# As seen below, we begin by constructing and imaging the basic
# edge inner product line matrix.
#
from discretize import TensorMesh
import matplotlib.pyplot as plt
import numpy as np
#
h = np.ones(2)
mesh = TensorMesh([h, h, h])
Me = mesh.get_edge_inner_product_line()
#
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)
ax.imshow(Me.todense())
ax.set_title('Basic Edge Inner Product Line Matrix', fontsize=18)
plt.show()
#
# Next, we consider the case where the physical properties
# are defined by diagnostic properties on mesh edges. For the isotropic case,
# we show the physical property tensor for a single cell.
#
# Define the diagnostic property values for x, y and z faces.
#
tau_x, tau_y, tau_z = 3, 2, 1
#
# Here construct and image the edge inner product line matrix for the isotropic case.
# Spy plots are used to demonstrate the sparsity of the matrix.
#
tau = np.r_[
    tau_x * np.ones(mesh.n_edges_x),
    tau_y * np.ones(mesh.n_edges_y),
    tau_z * np.ones(mesh.n_edges_z)
]
M = mesh.get_edge_inner_product_line(tau)
#
# Then plot the sparse representation,
#
fig = plt.figure(figsize=(4, 4))
ax1 = fig.add_subplot(111)
ax1.imshow(M.todense())
ax1.set_title("M (isotropic)", fontsize=16)
plt.show()
