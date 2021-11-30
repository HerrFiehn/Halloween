from turtle import *
from random import *
from time import *

speed(0)

f = 10

hideturtle()

bgcolor("black")

penup()
goto(-270, 0)
pendown()

color("white")

fillcolor("white")

def H ():
    begin_fill()

    forward(10)
    left(90)
    forward(35)
    right(90)
    forward(30)
    right(90)
    forward(35)
    left(90)
    forward(10)
    left(90)
    forward(90)
    left(90)
    forward(10)
    left(90)
    forward(35)
    right(90)
    forward(30)
    right(90)
    forward(35)
    left(90)
    forward(10)
    left(90)
    forward(90)

    end_fill()

def A ():
    begin_fill()

    forward(10)
    left(90)
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    left(90)
    forward(10)
    left(90)
    forward(90)
    left(90)
    forward(50)
    left(90)
    forward(90)
    left(90)
    forward(10)
    left(90)
    penup()
    forward(45)
    pendown()

    end_fill() 

    fillcolor("black")

    begin_fill()

    right(90)
    for step in range(4):
        forward(30)
        left(90)

    end_fill()

def L ():
    fillcolor("white")
    begin_fill()

    forward(50)
    left(90)
    forward(20)
    left(90)
    forward(35)
    right(90)
    forward(70)
    left(90)
    forward(15)
    left(90)
    forward(90)

    end_fill()   

def O ():
    fillcolor("white")
    begin_fill()

    forward(50)
    left(90)
    forward(90)
    left(90)
    forward(50)
    left(90)
    forward(90)
    left(90)
    end_fill()
    penup()
    forward(10)
    left(90)
    forward(20)
    right(90)
    pendown()
    fillcolor("black")
    begin_fill()
    forward(30)
    left(90)
    forward(50)
    left(90)
    forward(30)
    left(90)
    forward(50)

    end_fill()

def W ():
    fillcolor("white")
    begin_fill()

    forward(50)
    left(90)
    forward(90)
    left(90)
    forward(10)
    left(90)
    forward(70)
    right(90)
    forward(10)
    right(90)
    forward(40)
    left(90)
    forward(10)
    left(90)
    forward(40)
    right(90)
    forward(10)
    right(90)
    forward(70)
    left(90)
    forward(10)
    left(90)
    forward(90)

    end_fill()

def E ():
    fillcolor("white")

    begin_fill()
    forward(50)
    left(90)
    forward(20)
    left(90)
    forward(40)
    right(90)
    forward(15)
    right(90)
    forward(20)
    left(90)
    forward(20)
    left(90)
    forward(20)
    right(90)
    forward(15)
    right(90)
    forward(40)
    left(90)
    forward(20)
    left(90)
    forward(50)
    left(90)
    forward(90)

    end_fill()

def N ():
    fillcolor("white")

    begin_fill()
    penup()
    forward(50)
    left(90)
    forward(90)
    left(90)
    forward(50)
    left(90)
    forward(90)
    left(90)
    pendown()
    end_fill()

    penup()

    forward(10)

    fillcolor("black")

    begin_fill()

    forward(30)
    left(120)
    forward(50)
    left(145)
    forward(40)


    end_fill()

    penup()

    right(90)
    forward(10)
    right(90)
    forward(90)
    right(90)
    forward(50)
    left(180)
    forward(10)

    pendown()

    fillcolor("black")

    begin_fill()
    penup()
    forward(30)
    left(120)
    forward(50)
    left(145)
    forward(40)
    pendown()
    end_fill()

sleep(3)


H()

penup()

left(90)
forward(60)

pendown()

A()

penup()

right(90)
forward(45)
left(90)
forward(50)

pendown()

L()

penup()

left(90)
forward(60)

pendown()

L()

penup()

left(90)
forward(60)

pendown()

O()

penup()

forward(20)
left(90)
forward(50)

pendown()

W()

penup()

left(90)
forward(60)

pendown()

E()

penup()

left(90)
forward(60)

pendown()

E()

penup()

left(90)
forward(60)

pendown()

N()


sleep(3)

speed(0)

penup()

goto(0, 0)

pendown()

clear()

right(80)

def Eule():
    fillcolor("saddlebrown")

    begin_fill()

    left(45)
    forward(50)
    left(45)
    forward(30)
    left(135)
    forward(10)
    right(45)
    forward(40)
    right(45)
    forward(10)
    left(135)
    forward(30)
    left(45)
    forward(50)

    end_fill()

    penup()

    left(45)
    left(180)
    forward(15)
    right(90)
    forward(45)

    pendown()

    right(90)
    
    color("black")

    fillcolor("orange")

    begin_fill()

    circle(5)

    end_fill()

    penup()

    forward(15)

    pendown()

    color("black")

    fillcolor("darkorange")

    begin_fill()

    circle(5)

    end_fill()  

def Kürbis():
    fillcolor("dark orange")

    begin_fill()

    circle(40)

    end_fill()

    left(90)
    forward(30)
    left(90)
    forward(20)
    right(180)

    fillcolor("black")

    begin_fill()

    for step in range(2):
        forward(40)
        right(90)
        forward(10)
        right(90)

    end_fill()

    forward(10)

    right(90)

    fillcolor("darkorange")

    begin_fill()

    for step in range(4):
        forward(2.5)
        left(90)

    end_fill()    
   
    left(90)

    forward(5)

    right(90)

    fillcolor("darkorange")

    begin_fill()

    for step in range(4):
        forward(3.5)
        left(90)

    end_fill()    
   
    left(90)

    forward(15)

    right(90)

    fillcolor("darkorange")

    begin_fill()

    for step in range(4):
        forward(3)
        left(90)

    end_fill()

    left(90)

    forward(5)
    right(90)
    forward(10)
    right(90)
    forward(10)

    right(90)

    fillcolor("darkorange")

    begin_fill()

    for step in range(4):
        forward(2)
        left(90)

    end_fill()

    left(90)

    forward(20)
    right(90)
    forward(10)

    forward(20)
    right(90)

    fillcolor("crimson")

    begin_fill()

    for step in range(4):
        forward(7.5)
        left(90)

    end_fill()

    forward(20)

    fillcolor("crimson")

    begin_fill()

    for step in range(4):
        forward(7.5)
        left(90)

    end_fill()

speed(0)


penup()
goto(-300,100)
pendown()

begin_fill()
fillcolor("saddle brown")
forward(600)
right(90)
forward(350)
right(90)
forward(600)
right(90)
forward(350)
end_fill()


penup()
goto(-100,-250)
pendown()


fillcolor("dark goldenrod")
begin_fill()
forward(150)
left(90)
forward(110)
left(90)
forward(150)
end_fill()

penup()
goto(-110,-175)
pendown()
fillcolor("yellow")
begin_fill()
circle(5)
end_fill()

penup()
goto(-300,100)
pendown()
fillcolor("sienna")
begin_fill()
left(114)
forward(330)
right(48)
forward(330)
end_fill()
penup()

goto(-30,-250)
begin_fill()
fillcolor("gray")
pendown()
left(114)
forward(180)
right(90)
forward(270)
right(90)
forward(180)
rt(90)
forward(270)
rt(90)
forward(180)
rt(90)
forward(270)
rt(90)
forward(10)
rt(90)
end_fill()

speed(0)
for Garagenstreifen in range(8):
    forward(270)
    left(90)
    forward(10.5)
    left(90)
    forward(270)
    right(90)
    forward(10.5)
    right(90)

speed(10)

penup()
goto(-210,45)
left(180)
pendown()

def fenster():
    begin_fill()
    fillcolor("gold")
    forward(100)
    right(90)
    forward(100)
    rt(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(45)
    end_fill()


fenster()

def fenster_dinger():
  
        begin_fill()
        fillcolor("gray")
        rt(90)
        forward(45)
        rt(90)
        forward(45)
        lt(90)
        forward(5)
        left(90)
        forward(45)
        rt(90)
        forward(50)
        lt(90)
        forward(5)
        lt(90)
        forward(45)
        forward(5)
        rt(90)
        forward(50)
        left(90)
        forward(5)
        left(90)
        forward(50)
        rt(90)
        forward(45)
        end_fill()

fenster_dinger()

right(90)

penup()

goto(15,45)

pendown()

fenster()
fenster_dinger()
