# Here we generate a basic 2D triangular mesh, by triangulating a rectangular domain.
#
from discretize import SimplexMesh
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri
#
# First we define the nodes of our mesh
#
X, Y = np.mgrid[-20:20:21j, -10:10:11j]
nodes = np.c_[X.reshape(-1), Y.reshape(-1)]
#
# Then we triangulate the nodes, here we use matplotlib, but you could also use
# scipy's Delaunay, or any other triangular mesh generator. Essentailly we are
# creating every node in the mesh, and a list of triangles/tetrahedrals defining which
# nodes make of each cell.
#
triang = tri.Triangulation(nodes[:, 0], nodes[:, 1])
simplices = triang.triangles
#
# Finally we can assemble them into a SimplexMesh
#
mesh = SimplexMesh(nodes, simplices)
mesh.plot_grid()
plt.show()
