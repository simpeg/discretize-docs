import discretize
from discretize import utils

cs, nc, npad = 20., 30, 8
hx = utils.meshTensor([(cs, npad+10, -0.7), (cs, nc), (cs, npad, 1.3)])
hz = utils.meshTensor([(cs, npad ,-1.3), (cs, nc), (cs, npad, 1.3)])
mesh = discretize.CylMesh([hx, 1, hz], x0=[0, 0, -hz.sum()/2])
mesh.plotGrid()