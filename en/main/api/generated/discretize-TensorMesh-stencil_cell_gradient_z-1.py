# Below, we demonstrate how to set boundary conditions for the
# z-component cell gradient stencil, construct the operator and apply it
# to a discrete scalar quantity. The mapping of the operator and
# its sparsity is also illustrated.
#
# We start by importing the necessary packages and modules.
#
from discretize import TensorMesh
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
#
# We then construct a mesh and define a scalar function at cell
# centers. In this case, the scalar represents some block within
# a homogeneous medium.
#
# Create a uniform grid
#
h = np.ones(40)
mesh = TensorMesh([h, h, h], "CCC")
#
# Create a discrete scalar at cell centers
#
centers = mesh.cell_centers
phi = np.zeros(mesh.nC)
k = (
    (np.abs(mesh.cell_centers[:, 0]) < 10.) &
    (np.abs(mesh.cell_centers[:, 1]) < 10.) &
    (np.abs(mesh.cell_centers[:, 2]) < 10.)
)
phi[k] = 1.
#
# Before constructing the operator, we must define
# the boundary conditions; zero Neumann for our example. Even though
# we are only computing the difference along z, we define boundary
# conditions for all boundary faces. Once the
# operator is created, it is applied as a matrix-vector product.
#
mesh.set_cell_gradient_BC(['neumann', 'neumann', 'neumann'])
Gz = mesh.stencil_cell_gradient_z
diff_phi_z = Gz @ phi
#
# Now we plot the original scalar, and the differencing taken along the
# z-axis for a slice at y = 0.
#
# .. collapse:: Expand to show scripting for plot
#
fig = plt.figure(figsize=(13, 5))
ax1 = fig.add_subplot(121)
mesh.plot_slice(phi, ax=ax1, normal='Y', slice_loc=0)
ax1.set_title("Scalar at cell centers", fontsize=14)
ax2 = fig.add_subplot(122)
v = np.r_[np.zeros(mesh.nFx+mesh.nFy), diff_phi_z]  # Define vector for plotting fun
mesh.plot_slice(v, ax=ax2, v_type='Fz', normal='Y', slice_loc=0)
ax2.set_title("Difference (z-axis)", fontsize=14)
plt.show()
#
# The z-component cell gradient stencil is a sparse differencing matrix
# that maps from cell centers to z-faces. To demonstrate this, we provide
# a spy plot
#
# .. collapse:: Expand to show scripting for plot
#
fig = plt.figure(figsize=(9, 9))
ax1 = fig.add_subplot(111)
ax1.spy(mesh.stencil_cell_gradient_z, ms=1)
ax1.set_title("Spy Plot", fontsize=16, pad=5)
ax1.set_xlabel("Cell Index", fontsize=12)
ax1.set_ylabel("Z-Face Index", fontsize=12)
plt.show()
