# We create a simple mesh and refine the TreeMesh such that all cells that
# intersect the line segment path are at the given levels.
#
import discretize
import matplotlib.pyplot as plt
import matplotlib.patches as patches
tree_mesh = discretize.TreeMesh([32, 32])
tree_mesh.max_level
# Expected:
## 5
#
# Next we define the points along the line and the level we want to refine to,
# and refine the mesh.
#
segments = np.array([[0.1, 0.3], [0.3, 0.9], [0.8, 0.9]])
levels = 5
tree_mesh.refine_line(segments, levels)
#
# Now lets look at the mesh, and overlay the line on it to ensure it refined
# where we wanted it to.
#
ax = tree_mesh.plot_grid()
ax.plot(*segments.T, color='C1')
plt.show()
