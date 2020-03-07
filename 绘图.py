from matplotlib import pyplot as  pl
import numpy as np
import math
x=np.arange(1,10,0.001)
y=[math.sin(each) for each in x]
pl.plot(x,y,'o')
pl.show()
