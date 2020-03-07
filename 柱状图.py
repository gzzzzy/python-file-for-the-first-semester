import numpy as np
import pygal as pg
x=np.arange(0,10,0.5)
y=np.sin(x)
hist=pg.Bar()
hist.add('',y)
hist.title='sin function'
hist.x_labels=[str(each) for each in x]
hist.x_title='x'
hist.y_title='sin(x)'
hist.render_to_file('sin.svg')
