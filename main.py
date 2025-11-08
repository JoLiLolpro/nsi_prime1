from turtle import *
from random import*

LCouleur = [
"Lavender",
"Turquoise",
"Coral",
"SkyBlue",
"Aqua",
"Salmon",
"Teal",
"Gold",
"Indigo"
]

legal_epeseur_values = [18, 26, 36]
legal_hauteur_values = [70, 80, 100]

class bibliotheque(Turtle):
    def gotos(self, x, y):
        """meme chose que goto() mais avec penup() inclus"""
        self.penup()
        self.goto(x,y)
        self.pendown()

    def calcul_epeseur_livres(self):
        """ont va calaculer les epaisseur des livres pour que ca rentre dans l'etagere, ont decide aussi si un livre va etre pencher ou non"""
        Liste_Taille_Livre = []
        total_livre = 0 # represente le current total des livres
        while True:
            if random() < 0.20 and (not Liste_Taille_Livre or Liste_Taille_Livre[-1] != -1): # livre pencher a 20% de chance, le livre d'avant ne peut pas etre aussi pencher
                taille =-1 # valeur qu'on pourra reconnaitre plus tard
                Livre_et_bordure = 36+4
            else:
                taille = choice(legal_epeseur_values) # represente la taille du livre
                Livre_et_bordure = taille+4 # le livre ET la bordure
            total_livre += Livre_et_bordure
            if total_livre > (560-20): # ont calcule si ont ne depasse pas le cadre
                return Liste_Taille_Livre
            Liste_Taille_Livre.append(taille)

    def cadre(self, hauteur):
        """dessine le grand cadre marron qui correspond au meuble"""
        self.gotos(-300, -300) # va a gauche pour le cadre
        self.color('#5C4033') # marron mais vraiment marron
        self.begin_fill()
        for i in range(2):
            self.fd(560)
            self.left(90)
            self.fd(hauteur)
            self.left(90)
        self.end_fill()

    def contoure(self, epeseur, hauteur):
        """fait le contoure noir de chaque livres"""
        self.color('black')
        self.begin_fill()
        for i in range(2):
            self.fd(epeseur+4)
            self.left(90)
            self.fd(hauteur+4)
            self.left(90)
        self.end_fill()
        # va a l'interieur de cadre pour draw le livre
        self.fd(2)
        self.left(90)
        self.fd(2)
        self.right(90)

    def livre_transition(self, epeseur):
        """repositionne la tortue apres chaque livres"""
        self.penup()
        self.fd(epeseur+2)
        self.right(90)
        self.fd(2)
        self.left(90)
        self.pendown()

    def livre(self, couleur, epeseur, hauteur, angle=360):
        """dessine un livre avec comme multiplicateur epeseur et hauteur"""
        self.contoure(epeseur, hauteur)
        self.color(couleur)
        self.begin_fill()
        for i in range(2):
            self.fd(epeseur)
            self.left(90)
            self.fd(hauteur)
            self.left(90)
        self.end_fill()

    def livre_pencher(self, hauteur):
        """fait un livre pencher"""
        position = self.position()
        self.penup()
        self.left(90)
        self.fd(4)
        self.right(100)
        self.pendown()
        self.livre(choice(LCouleur), 18, choice(legal_hauteur_values))
        self.gotos(position[0]+2,position[1]+2)
        self.left(10)

    def livres_avec_un_S(self, livres_liste):
        """fait les livres sur l'etagere"""
        for k in range(len(livres_liste)):
            epeseur_temp = livres_liste[k]
            if epeseur_temp == -1:
                self.livre_pencher(choice(legal_hauteur_values))
                epeseur_temp = 36
            else:
                self.livre(choice(LCouleur), epeseur_temp, choice(legal_hauteur_values))
            self.livre_transition(epeseur_temp)

    def etageres(self, nombre):
        """dessine un cadres puis des etageres composee de livres"""
        self.cadre(120*nombre)
        self.gotos(-300+10, -300+10) # ecart de 10px pour le premier livre
        for i in range(1, nombre+1):
            livres_liste = self.calcul_epeseur_livres()
            self.livres_avec_un_S(livres_liste)
            self.gotos(-300+10, -300+i*120)


#oui = bibliotheque()
#oui.speed(0)
#oui.etageres(4)
exitonclick()

