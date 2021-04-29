import discretize
import numpy as np
import matplotlib.pyplot as plt
mesh = discretize.TensorMesh([np.ones(n) for n in [2,3]])
mesh.plot_grid(centers=True, show_it=True)
print(mesh.n_cells)
