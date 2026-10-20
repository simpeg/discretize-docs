# In 2D we define the surface as a line segment, which we would like to refine
# along.
#
import discretize
import matplotlib.pyplot as plt
import matplotlib.patches as patches
mesh = discretize.TreeMesh([32, 32])
#
# This surface is a simple sine curve, which we would like to pad with at least
# 2 cells vertically below at the maximum level, and 3 cells below that at the
# second highest level.
#
x = np.linspace(0.2, 0.8, 51)
z = 0.25*np.sin(2*np.pi*x)+0.5
xz = np.c_[x, z]
mesh.refine_surface(xz, -1, [[0, 2], [0, 3]])
#
ax = mesh.plot_grid()
ax.plot(x, z, color='C1')
plt.show()
#
# In 3D we define a grid of surface locations with there corresponding elevations.
# In this example we pad 2 cells at the finest level below the surface, and 3
# cells down at the next level.
#
mesh = discretize.TreeMesh([32, 32, 32])
x, y = np.mgrid[0.2:0.8:21j, 0.2:0.8:21j]
z = 0.125*np.sin(2*np.pi*x) + 0.5 + 0.125 * np.cos(2 * np.pi * y)
points = np.stack([x, y, z], axis=-1).reshape(-1, 3)
mesh.refine_surface(points, -1, [[0, 0, 2], [0, 0, 3]])
#
v = mesh.cell_levels_by_index(np.arange(mesh.n_cells))
fig, axs = plt.subplots(1, 3, figsize=(12,4))
mesh.plot_slice(v, ax=axs[0], normal='x', grid=True, clim=[2, 5])
mesh.plot_slice(v, ax=axs[1], normal='y', grid=True, clim=[2, 5])
mesh.plot_slice(v, ax=axs[2], normal='z', grid=True, clim=[2, 5])
plt.show()
