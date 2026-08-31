import numpy as n
import math
import matplotlib.pyplot as mp

from mpl_toolkits.mplot3d import Axes3D
def d2():
    x=n.random.normal(loc=5, scale=2, size=100)
    y= n.sin(x)+ n.log(x)

    mp.plot(x,y,label="sinus&ln",c="green")

    mp.xlabel("abscisse")
    mp.ylabel("ordonnee")

    print(y)
    mp.legend()
    mp.grid(True)
    mp.show()


def d3():
    x = n.linspace(0.1, 10, 100)  # Éviter log(0)
    y = n.sin(x)
    z = n.sin(x) + n.log(x)

    fig = mp.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, color='green', label='z = sin(x) + ln(x)')

    ax.set_xlabel('x')
    ax.set_ylabel('sin(x)')
    ax.set_zlabel('z')
    ax.set_title("Courbe 3D : z = sin(x) + ln(x)")
    ax.legend()
    mp.show()

def principal():
    while True:
        choix=int(input("Taper 1 pour tracer une courbe en 2D\n, 2 pour tracer une courbe en 3D \n"))
        if(choix==1):
            d2()
        if(choix==2):
            d3()
        else:
            print("choix non valide")
        
            break

5



