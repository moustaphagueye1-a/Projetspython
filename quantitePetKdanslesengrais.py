def arbre():
    print("Vous etes dans la fonctionnalite calcul de la quantite de phosphate P \n ")
    Q = float(input("Donner la quantite de P2O5 dans l engrais \n"))
    Z = (100 * (Q * (62 / 142))) / 20
    
    print("La quantite de P dans l engrais ", Z)
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
    
    
        
    
    
    
    
    
    

