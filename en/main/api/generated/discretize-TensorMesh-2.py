import discretize
mesh = discretize.TensorMesh([
    [(10, 10, -1.3), (10, 40), (10, 10, 1.3)],
    [(10, 10, -1.3), (10, 20)]
])
mesh.plot_grid()