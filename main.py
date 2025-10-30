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

legal_epeseur_values = [0.50, 1]
legal_hauteur_values = [0.70, 1]

class toto(Turtle):
    def gotos(self, x, y):
        """meme chose que goto() mais avec penup() inclus"""
        self.penup()
        self.goto(x,y)
        self.pendown()

    def cadre(self, hauteur):
        """dessine le grand cadre marron qui correspond au meuble"""
        self.gotos(-300, -300) # va a gauche pour le cadre
        self.color('#453107') # marron mais vraiment marron
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
            self.fd(36*epeseur+4)
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
        self.fd(36*epeseur+2)
        self.right(90)
        self.fd(2)
        self.left(90)

    def livre(self, couleur, epeseur, hauteur, angle=360):
        """dessine un livre avec comme multiplicateur epeseur et hauteur"""
        self.contoure(epeseur, hauteur)
        self.color(couleur)
        self.begin_fill()
        for i in range(2):
            self.fd(36*epeseur)
            self.left(90)
            self.fd(100*hauteur)
            self.left(90)
        self.end_fill()

    def etageres(self, nombre):
        """dessine une etagere composee de livres"""
        self.gotos(-300+10, -300+10) # ecart de 10px pour le premier livre
        for i in range(1, nombre+1):
            while self.xcor() < -300+560-10:
                epeseur_temp = choice(legal_epeseur_values)
                self.livre(choice(LCouleur), epeseur_temp, choice(legal_hauteur_values))
                self.livre_transition(epeseur_temp)
            self.gotos(-300+10, -300+i*120)

oui = toto()
oui.speed(0)
oui.cadre(600)
oui.etageres(2)
exitonclick()
