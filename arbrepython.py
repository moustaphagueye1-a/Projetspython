def arbre():
    print("Vous etes dans la fonctionnalite calcul arbe \n ")
    L=float(input("Donner la longeur\n"))
    l=float(input("Donner la largeur\n"))
    d=float(input("Donner la densite souhaitee\n"))
    print("Le nombre d arbre est ",(L*l)*d)
def co2():
    print("VOUS ETES DANS LA FONCTIONNALITE DE CALCULE DE CO2 CAPTURE")
    Q=float(input("Donner vos objectifs environnementaux en terme de co2 capture\n"))
    d=float(input("Donner la densite de vos arbres en m2\n"))
    print("vous devez planter a l hectare\n",d*10000)
    print("vous pourez capturer la quantite de c02 a l hectare \n",d*10000*Q)
def principal():
    while True:
       choix=int(input("Taper 1 pour trouver le nonbre d arbre \n 2 pour  trouver la quantite de co2 capture\n 3 pour quiter"))
       if(choix==1):
           arbre()
       if(choix==2):
           co2()
       if(choix==3):
            break
    
    
        
    
    
    
    
    
    

