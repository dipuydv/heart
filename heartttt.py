import turtle
from turtle import *
wn=Screen()
wn.bgcolor("black")
t=turtle.Turtle()
t.pencolor("purple")
def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)
def heart():
    t.fillcolor('red')
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()
heart()
t.ht()
def write(message,pos):
    x,y=pos
    t.penup()
    t.goto(x,y)
    t.color('white')
    style=('Stencil Std', 19, 'italic')
    t.write(message,font=style)
write('I',(-68,95))
write('L',(-55,95))
write('O',(-42,95))
write('V',(-25,95))
write('E',(-9,95))
write('C',(-34,60))
write('O',(-18,60))
write('D',(0,60))
write('I',(17,60))
write('N',(22,60))
write('G',(39
           ,60))
main.loop()
