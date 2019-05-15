import discretize

hx = np.array([1, 1, 1])
hy = np.array([1, 2])
hz = np.array([1, 1, 1, 1])

mesh = discretize.TensorMesh([hx, hy, hz])
mesh.plotGrid()