# We create a simple mesh and refine the TreeMesh such that all cells that
# intersect the line segment path are at the given levels.
#
import discretize
import matplotlib.pyplot as plt
import matplotlib.patches as patches
tree_mesh = discretize.TreeMesh([32, 32, 32])
tree_mesh.max_level
# Expected:
## 5
#
# Next we define the points along the line and the level we want to refine to,
# and refine the mesh.
#
tetra = [
    [0.32, 0.21, 0.15],
    [0.82, 0.19, 0.34],
    [0.14, 0.82, 0.29],
    [0.32, 0.27, 0.83],
]
levels = 5
tree_mesh.refine_tetrahedron(tetra, levels)
#
# Now lets look at the mesh, checking how the refine function proceeded.
#
levels = tree_mesh.cell_levels_by_index(np.arange(tree_mesh.n_cells))
ax = plt.gca()
tree_mesh.plot_slice(levels, normal='z', slice_loc=0.2, grid=True, ax=ax)
plt.show()
