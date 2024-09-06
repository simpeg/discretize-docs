# Here we compute the values of a vector function discretized to the edges.
# We then create an averaging operator to approximate the function on
# the faces.
#
# We start by importing the necessary packages and defining a mesh.
#
from discretize import TensorMesh
import numpy as np
import matplotlib.pyplot as plt
h = 0.5 * np.ones(40)
mesh = TensorMesh([h, h], x0="CC")
#
# Create a discrete vector on mesh edges
#
edges = mesh.edges
u_ex = -(edges[:, 1] / np.sqrt(np.sum(edges ** 2, axis=1))) * np.exp(
    -(edges[:, 0] ** 2 + edges[:, 1] ** 2) / 6 ** 2
)
u_ey = (edges[:, 0] / np.sqrt(np.sum(edges ** 2, axis=1))) * np.exp(
    -(edges[:, 0] ** 2 + edges[:, 1] ** 2) / 6 ** 2
)
u_e = np.c_[u_ex, u_ey]
#
# Next, we construct the averaging operator and apply it to
# the discrete vector quantity to approximate the value at the faces.
#
Aef = mesh.average_edge_to_face
u_f = Aef @ u_e
#
# Plot the results,
#
fig = plt.figure(figsize=(11, 5))
ax1 = fig.add_subplot(121)
proj_ue = mesh.project_edge_vector(u_e)
mesh.plot_image(proj_ue, ax=ax1, v_type="E", view='vec')
ax1.set_title("Variable at edges", fontsize=16)
ax2 = fig.add_subplot(122)
proj_uf = mesh.project_face_vector(u_f)
mesh.plot_image(proj_uf, ax=ax2, v_type="F", view='vec')
ax2.set_title("Averaged to faces", fontsize=16)
plt.show()
#
# Below, we show a spy plot illustrating the sparsity and mapping
# of the operator
#
fig = plt.figure(figsize=(9, 9))
ax1 = fig.add_subplot(111)
ax1.spy(Aef, ms=1)
ax1.set_title("Edge Index", fontsize=12, pad=5)
ax1.set_ylabel("Face Index", fontsize=12)
plt.show()
