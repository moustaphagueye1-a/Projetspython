import random

# Variable globale pour stocker le gain
w = 0

def gainde():
    global w
   
    tirage = random.randint(1, 6)
    if ((tirage==5)or (tirage==2)):
        w=w+1
        print("Gain\n")
    else:
        print("Perte\n")
def dix():
    global w
    
    
    for _ in range(10):
        tirage = random.randint(1, 6)
        if ((tirage==5)or (tirage==2)):
               w=w+1
               print("Gain\n")
        else:
             print("Perte\n")
def dof():
    
    
    t = 0
    for _ in range(1000):
        
   
        tirage = random.randint(1, 6) 
        if ((tirage==5)or (tirage==2)):
            
            
            t=t+1
    print(" Sur 1000 tentative , on a gagne ", t,"fois")
    
            
       
        
        
       

        
