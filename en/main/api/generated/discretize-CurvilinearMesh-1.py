import discretize
X, Y = discretize.utils.exampleLrmGrid([3,3],'rotate')
mesh = discretize.CurvilinearMesh([X, Y])
mesh.plot_grid(show_it=True)