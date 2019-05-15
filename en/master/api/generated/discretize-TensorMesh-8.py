import discretize
from pymatsolver import Solver
import numpy as np
hx = [(5, 2, -1.3), (2, 4), (5, 2, 1.3)]
hy = [(2, 2, -1.3), (2, 6), (2, 2, 1.3)]
hz = [(2, 2, -1.3), (2, 6), (2, 2, 1.3)]
M = discretize.TensorMesh([hx, hy, hz])
q = np.zeros(M.vnC)
q[[4, 4], [4, 4], [2, 6]]=[-1, 1]
q = discretize.utils.mkvc(q)
A = M.faceDiv * M.cellGrad
b = Solver(A) * (q)
M.plotSlice(M.cellGrad*b, 'F', view='vec', grid=True, showIt=True, pcolorOpts={'alpha':0.8})