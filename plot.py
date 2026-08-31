import matplotlib.pyplot as plt # l importation du module matplotlib et sa "nomination" en plt 
x=[1,9,4,2,6,7]# La definition de la liste x
y=[4,1,7,13,4,6]# La definition de la liste y
plt.plot(x,y,label="Courbe ",lw=5,ls='--',c="red")#pour definir les parametres de la courbe comme la couleur .
plt.legend()#pour definir  la legende de la courbe
plt.xlabel("abscise")#pour Etiquetter la courbe
plt.ylabel("ordonnee ")#pour Etiquetter la courbe
plt.title("Mon titre ")#pour titrer la courbe 
plt.show()#affichage de la  courbe


