from modulecalcule import addition , soustraction , multiplication , division
def principal():
    while True:
       choix=int(input("Taper 1 pour additionner  \n 2 pour soustraire  \n 3 pour faire le produit\n 4 pour diviser \n 5 pour quitter"))
       if(choix==1):
           addition()
       elif(choix==2):
           soustraction()
       elif(choix==3): 
           multiplication()
       elif(choix==4):
           division()
       elif(choix==5):
            break
if __name__ == "__moduleresultat_":
    principal()
   
       
        
    
    
        
            
    
