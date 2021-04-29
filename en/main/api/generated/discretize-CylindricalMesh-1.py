import discretize
from discretize import utils

cs, nc, npad = 20., 30, 8
hx = utils.unpack_widths([(cs, npad+10, -0.7), (cs, nc), (cs, npad, 1.3)])
hz = utils.unpack_widths([(cs, npad ,-1.3), (cs, nc), (cs, npad, 1.3)])
mesh = discretize.CylindricalMesh([hx, 1, hz], origin=[0, 0, -hz.sum()/2])
mesh.plot_grid()