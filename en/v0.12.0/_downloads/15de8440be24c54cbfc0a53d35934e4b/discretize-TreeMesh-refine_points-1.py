# Given a set of points, we want to refine the tree mesh around these points to
# a prescribed level with a certain amount of padding.
#
import discretize
import matplotlib.pyplot as plt
import matplotlib.patches as patches
mesh = discretize.TreeMesh([32, 32])
#
# Now we want to refine to the maximum level with 1 cell padding around the point,
# and then refine at the second highest level with at least 3 cells beyond that.
#
points = np.array([[0.1, 0.3], [0.6, 0.8]])
padding = [1, 3]
mesh.refine_points(points, -1, padding)
#
ax = mesh.plot_grid()
ax.scatter(*points.T, color='C1')
plt.show()
