import discretize
import numpy as np
M = discretize.TensorMesh([20, 20])
v = np.sin(M.gridCC[:, 0]*2*np.pi)*np.sin(M.gridCC[:, 1]*2*np.pi)
M.plotImage(v, showIt=True)