import numpy as np

a = np.empty((3,3))

print(a)

for i in a:
    for j in i:
        print(j)


class Jeux:
    def __init__(self, move, grille):
        self.move = move
        self.grille = []
        self.joueur1 = joueur1
        self.joueur2 = joueur2 
        
   def bord(self):
        print(ligne1 = [None] * 3)
        print(ligne2 = [None] * 3)
        print(ligne3 = [None] * 3)
    
    

    def play():
        while cases non remplies and 3 signes non aligné      
            premier joueur joue :
                le mettre dans la grille
                case bloqué
            deuxième joueur joue (sauf dans la case bloqué)
                le mettre dans la grille
            
        si toute les cases sont remplie ==> break ==> match nul
        
        si 3 signe aligné ==> break ==> un gagnant
        
        
        
        
    def recommencer():
        quand partie fini, possibilité de reprendre le jeux

class Joueur:
    def __init__(self, user):
        self.user = user
        self.symbole = "" 

    def choice(self):
        choix = ""
        while choix != "X" and choix != "0" :
            choix = input("Quel signe tu veux entre X et O ?")
        return choix
        """
        if choix == "X":
            associer au joueur 1
            joueur1.symbole = "X"
            joueur 2 est du signe de O
        elif choix == "O":
            associer au joueur O
            joueur 2 == X
        else :
            pas bon, retente
            """

joueur1 = Joueur("")
joueur2 =

