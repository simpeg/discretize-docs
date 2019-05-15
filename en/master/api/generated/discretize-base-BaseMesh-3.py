import discretize
import numpy as np
M = discretize.TensorMesh([np.ones(n) for n in [2,3]])
M.plotGrid(faces=True, showIt=True)