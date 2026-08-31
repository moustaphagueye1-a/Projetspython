import numpy as n
import matplotlib.pyplot as mp
x=n.random.normal(0,2*n.pi,100)
y=n.sin(x)
z=n.cos(x)
mp.plot(x,y,label="sinus",c="green")
mp.plot(x,z,label="cosunus",c="black")
mp.xlabel("abscisse")
mp.ylabel("ordonnee")

print(y)
mp.legend()
mp.grid(True)
mp.show()
