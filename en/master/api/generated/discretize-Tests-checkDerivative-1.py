from discretize import Tests, utils
import numpy as np

def simplePass(x):
    return np.sin(x), utils.sdiag(np.cos(x))
Tests.checkDerivative(simplePass, np.random.randn(5))