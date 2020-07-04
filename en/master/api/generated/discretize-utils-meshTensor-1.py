import discretize
tx = [(10.0, 10, -1.3), (10.0, 40), (10.0, 10, 1.3)]
ty = [(10.0, 10, -1.3), (10.0, 40)]
mesh = discretize.TensorMesh([tx, ty])
mesh.plotGrid(show_it=True)