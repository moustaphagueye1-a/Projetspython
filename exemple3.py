import numpy as n
import matplotlib.pyplot as pl
for i in range(0,100,2):
    print(i)
x=n.arange(0,100,2)
y=n.cos(x)
pl.plot(x,y)
pl.xlabel("X ")  
pl.ylabel("Y ")
pl.show()
