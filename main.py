from turtle import *
import random

class toto(Turtle):
    def gotos(self, x, y):
        self.penup()
        self.goto(x,y)
        self.pendown()


    def cadre(self):
        self.gotos(0,0)
        couleur = self.color('#453107')
        self.begin_fill()
        self.fd(250)
        for i in range(2):
            self.left(90)
            self.fd(300)
            self.left(90)
            self.fd(500)
        self.end_fill()

    def livre(self, couleur, epeseur, angle):
        self.gotos(0,0)
        couleur = self.color(couleur)
        self.begin_fill()
        for i in range(2):
            self.fd(50*epeseur)
            self.left(90)
            self.fd(100)
            self.left(90)
            self.end_fill()

    def etageres(self, nombre):
        

oui = toto()
oui.speed(0)
oui.cadre()
oui.livre('blue', 1, 90)
exitonclick()
