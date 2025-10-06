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

class toto(Turtle):
    def gotos(self, x, y):
        self.penup()
        self.goto(x,y)
        self.pendown()


    def cadre(self, hauteur):
        self.color('#453107') # marron mais vraiment marron
        self.begin_fill()
        for i in range(2):
            self.fd(600)
            self.left(90)
            self.fd(hauteur)
            self.left(90)
        self.end_fill()

    def contoure(self, epeseur):
        self.color('black')
        self.begin_fill()
        for i in range(2):
            self.fd(50*epeseur+4)
            self.left(90)
            self.fd(100+4)
            self.left(90)
        self.end_fill()
        # va a l'interieur de cadre pour draw le livre
        self.fd(2)
        self.left(90)
        self.fd(2)
        self.right(90)


    def livre(self, couleur, epeseur, angle=360):
        self.contoure(epeseur)
        self.color(couleur)
        self.begin_fill()
        for i in range(2):
            self.fd(50*epeseur)
            self.left(90)
            self.fd(100)
            self.left(90)
        self.end_fill()
        self.fd(90+2+2)


    def etageres(self, nombre, hauteur):
        self.gotos(-300, 0) # va a gauche pour le cadre
        self.cadre(hauteur)
        self.gotos(-300+10, 0+10) # ecare de 10px pour le livre
        for i in range(1, nombre+1):
            for k in range(10):
                self.livre(choice(LCouleur), 1)
            self.gotos(-300+10, 0+i*120)
            print(i)

oui = toto()
#tracer(20)
oui.etageres(3,300)
exitonclick()
