import matplotlib.pyplot as plt
import discretize
plt.colorbar(plt.imshow(discretize.utils.random_model((50, 50), bounds=[-4, 0])))
plt.title('A very cool, yet completely random model.')
plt.show()