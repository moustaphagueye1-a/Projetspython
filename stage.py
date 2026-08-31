def addition():
    print(" Addition  \n ")
    a=float(input("Donner la premiere valeur  \n"))
    b=float(input("Donner la deuxieme valeur "))
    resultat=a+b
    print("Resultat =  ",resultat)
def soustraction ():
    print(" soustraction  \n ")
    a=float(input("Donner la premiere valeur  \n"))
    b=float(input("Donner la deuxieme valeur "))
    resultat=a-b
    print("Resultat =  ",resultat)
def multiplication  ():
    print(" multiplication  \n ")
    a=float(input("Donner la premiere valeur  \n"))
    b=float(input("Donner la deuxieme valeur "))
    resultat=a*b
    print("Resultat =  ",resultat)
def division  ():
    print(" division  \n ")
    
    a=float(input("Donner le numerateur a  \n"))
    b=float(input("Donner le denominateur b "))
    while b==0 :
        print("IMPOSSIBLE : LE DENOMINATEUR NE PEUT ETRE NUL ")
        b=float(input("Donner le denominateur b "))
        
    resultat=a / b
    print("Resultat =  ",resultat)
        
    


def principal():
    while True:
       choix=int(input("Taper 1 pour faire l addition \n 2 pour  trouver la soustraction \n 3 pour la multiplication \n 4 pour la division \n 5 pour quitter  "))
       if(choix==1):
           addition()
       if(choix==2):
            soustraction()
       if(choix==3):
            multiplication()
            

       if(choix==4):
           division()
       if(choix==5):
            break
principal()        
          
       
    
    
        
    
    
    
    
    
    

