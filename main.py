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

legal_epeseur_values = [18, 36]
legal_hauteur_values = [0.70, 1]

class toto(Turtle):
    def gotos(self, x, y):
        """meme chose que goto() mais avec penup() inclus"""
        self.penup()
        self.goto(x,y)
        self.pendown()

    def calcul_epeseur_livres(self):
        """en collaboration avec nintendo ont va calaculer les epaisseur des livres pour que ca rentre dans l'etagere"""
        luigi = []
        peach = 0
        while True:
            toad = choice(legal_epeseur_values) # toad represente la taille de livre
            mario = toad+4 # mario est plutot le livre ET la bordure
            peach += mario 
            if peach > 560-10: # ont calcule si ont ne depasse pas le cadre
                return luigi
            luigi.append(toad)

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
            self.fd(100*hauteur+4)
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

    def livre(self, couleur, epeseur, hauteur, angle=360):
        """dessine un livre avec comme multiplicateur epeseur et hauteur"""
        self.contoure(epeseur, hauteur)
        self.color(couleur)
        self.begin_fill()
        for i in range(2):
            self.fd(epeseur)
            self.left(90)
            self.fd(100*hauteur)
            self.left(90)
        self.end_fill()

    def etageres(self, nombre):
        """dessine une etagere composee de livres"""
        self.gotos(-300+10, -300+10) # ecart de 10px pour le premier livre
        for i in range(1, nombre+1):
            livres_liste = self.calcul_epeseur_livres()
            for k in range(len(livres_liste)):
                epeseur_temp = livres_liste[k]
                self.livre(choice(LCouleur), epeseur_temp, choice(legal_hauteur_values))
                self.livre_transition(epeseur_temp)
            self.gotos(-300+10, -300+i*120)


oui = toto()
oui.speed(0)
oui.cadre(700)
oui.etageres(4)
exitonclick()

