##example plotting some of the poly
import matplotlib.pyplot as plt
import numpy as np

x = np.array([i for i in range(0,10)],dtype=float)
#y = 6*x**4+3*x**3+3*x**2+2*x+10
y = x**2+2*x+3
plt.plot(x,y)
plt.show()