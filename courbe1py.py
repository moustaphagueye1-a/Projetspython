import numpy as n
import matplotlib.pyplot as pl
x=n.linspace(0,1000,360)
y=n.sin(x)
pl.plot(x,y)
print(y)
pl.show()
