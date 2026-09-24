import numpy as n
import matplotlib.pyplot as pl
x=n.linspace(0,10,100)
y=n.sin(x)
pl.plot(x,y)
print(y)
pl.grid(True)
pl.show()
