import discretize
X, Y = discretize.utils.exampleLrmGrid([3, 3], 'rotate')
M = discretize.CurvilinearMesh([X, Y])
M.plotGrid(show_it=True)