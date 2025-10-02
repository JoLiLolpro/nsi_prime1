from turtle import *
from random import*

class toto(Turtle):
    def gotos(self, x, y):
        self.penup()
        self.goto(x,y)
        self.pendown()


    def cadre(self, taille):
        self.color('#453107')
        self.fd(250)
        self.begin_fill()
        for i in range(2):
            self.left(90)
            self.fd(taille)
            self.left(90)
            self.fd(500)
        self.end_fill()
        self.pencolor('black')
        for i in range(2):
            self.left(90)
            self.fd(taille)
            self.left(90)
            self.fd(500)

    def livre(self, couleur, epeseur, angle=360):
        self.color('black')
        self.begin_fill()
        for i in range(2):
            self.fd(50*epeseur)
            self.left(90)
            self.fd(100)
            self.left(90)
        self.end_fill()
        self.fd(2)
        self.left(90)
        self.fd(2)
        self.right(90)
        self.color(couleur)
        self.begin_fill()
        for i in range(2):
            self.fd(50*epeseur-4)
            self.left(90)
            self.fd(100-2)
            self.left(90)
        self.fd(50*epeseur-4)
        self.end_fill()
        self.fd(-2)
        self.left(90)
        self.fd(-2)
        self.right(90)

    def etageres(self, nombre,taille):
        self.gotos(0,-300)
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
        self.cadre(taille)
        self.gotos(-230,-taille)
        for i in range(nombre):
            for i in range(10):
                self.livre(choice(LCouleur), 1)
            print("oui")
            self.gotos(-230,-280+i*120)

oui = toto()
oui.speed(0)
oui.etageres(3,280)
exitonclick()

