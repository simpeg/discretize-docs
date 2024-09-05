# Given a set of points, we want to refine the tree mesh with the bounding box
# that surrounds those points. The arbitrary points we use for this example are
# uniformly scattered between [3/8, 5/8] in the first and second dimension.
#
import discretize
import matplotlib.pyplot as plt
import matplotlib.patches as patches
mesh = discretize.TreeMesh([32, 32])
points = np.random.rand(20, 2) * 0.25 + 3/8
#
# Now we want to refine to the maximum level, with no padding the in `x`
# direction and `2` cells in `y`. At the second highest level we want 2 padding
# cells in each direction beyond that.
#
padding = [[0, 2], [2, 2]]
mesh.refine_bounding_box(points, -1, padding)
#
# For demonstration we, overlay the bounding box to show the effects of padding.
#
ax = mesh.plot_grid()
rect = patches.Rectangle([3/8, 3/8], 1/4, 1/4, facecolor='none', edgecolor='r', linewidth=3)
ax.add_patch(rect)
plt.show()
