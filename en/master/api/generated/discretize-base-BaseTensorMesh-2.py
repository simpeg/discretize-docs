import discretize
import numpy as np
mesh = discretize.TensorMesh([np.ones(n) for n in [2,3]])
mesh.plotGrid(nodes=True, showIt=True)

print(mesh.nN)