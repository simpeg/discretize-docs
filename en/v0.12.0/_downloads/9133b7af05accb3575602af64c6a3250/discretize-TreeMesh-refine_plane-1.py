# We create a simple mesh and refine the TreeMesh such that all cells that
# intersect the plane path are at the given levels. (In 2D, the plane is also a
# line.)
#
import discretize
import matplotlib.pyplot as plt
tree_mesh = discretize.TreeMesh([32, 32])
tree_mesh.max_level
# Expected:
## 5
#
# Next we define the origin and normal of the plane, and the level we want
# to refine to.
#
origin = [0, 0.25]
normal = [-1, -1]
level = -1
tree_mesh.refine_plane(origin, normal, level)
#
# Now lets look at the mesh, and overlay the plane on it to ensure it refined
# where we wanted it to.
#
ax = tree_mesh.plot_grid()
ax.axline(origin, slope=-normal[0]/normal[1], color='C1')
plt.show()
