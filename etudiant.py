etudiants = []
def ajoute():
    etudiant={
        "nom" : input("nom :" ),
        "prenom" : input("prenom :" ),
        "lieu de naissance ": input("lieu de naissance  :"  ),
        "date de naissance " : input(" date de naissance:" ),
        "Groupe TD" : input("Groupe TD :"  ),
        "numero carte d identite " : input("cni  :"  )
        
    }
    etudiants.append(etudiant)
    print("Etudiant ajoute . \n")
def afficher() :
    
    print(etudiants)
def chercher () :
   nin=int(input("Donner le numero de  carte d identite de la   personne a recherher  "))
   if w= 0:
       print("Etudiant non supprime .")







    


    


def principal():
    while True:
        choix=int(input("Taper 1 pour  pour ajouter un etudiant \n Taper 2 pour  pour afficher  la liste des  etudiants  . "))
        if(choix==1):
          ajoute()
        if(choix==2):
          afficher() 
principal()
       
