import discretize
import numpy as np
h1 = np.linspace(.1, .5, 3)
h2 = np.linspace(.1, .5, 5)
mesh = discretize.TensorMesh([h1, h2])
mesh.plotGrid(nodes=True, faces=True, centers=True, lines=True, show_it=True)