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
legal_hauteur_values = [70, 100]

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
            if random() < 0.2: # livre pencher 20% de chance
                toad = 0 # valeur qu'on pourra reconnaitre plus tard
                mario = 36+4
            else:
                toad = choice(legal_epeseur_values) # toad represente la taille de livre
                mario = toad+4 # mario est le livre ET la bordure
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

    def livre_pencher(self):
        self.livre("red", 36, 100)

    def livres_avec_un_S(self, livres_liste):
        """fait les livres sur l'etagere"""
        for k in range(len(livres_liste)):
            epeseur_temp = livres_liste[k]
            if epeseur_temp == 0:
                self.livre_pencher()
                epeseur_temp = 36
            else:
                self.livre(choice(LCouleur), epeseur_temp, choice(legal_hauteur_values))
            self.livre_transition(epeseur_temp)

    def etageres(self, nombre):
        """dessine une etagere composee de livres"""
        self.gotos(-300+10, -300+10) # ecart de 10px pour le premier livre
        for i in range(1, nombre+1):
            livres_liste = self.calcul_epeseur_livres()
            self.livres_avec_un_S(livres_liste)
            self.gotos(-300+10, -300+i*120)


oui = toto()
oui.speed(0)
oui.cadre(700)
oui.etageres(4)
exitonclick()

