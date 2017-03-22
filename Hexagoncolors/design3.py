from myPolygon import *
import turtle
alice=turtle.Turtle()
zeus=turtle.Turtle()
bob=turtle.Turtle()
turtle.colormode(255)
turtle.bgcolor("blue")
bob.speed(0)
alice.speed(0)
zeus.speed(0)

for times in range(10):
    bob.penup()
    bob.goto(-15,0)
    c=(0,times,0)
    bob.forward(0)
    bob.right(45)
    bob.forward(200)
    bob.pendown()
    bob.color(200,times,145)
    bob.begin_fill()
    polygon(bob,20,30)
    bob.end_fill()

for times in range(10):
    alice.penup()
    alice.goto(-15,0)
    c=(0,times,0)
    alice.forward(0)
    alice.right(45)
    alice.forward(200)
    alice.pendown()
    alice.color(200,times,times)
    alice.begin_fill()
    polygon(alice,10,40)
    alice.end_fill()


for times in range(10):
    zeus.penup()
    zeus.goto(-15,0)
    c=(0,times,0)
    zeus.forward(0)
    zeus.right(45)
    zeus.forward(200)
    zeus.pendown()
    zeus.color(times,144,times)
    zeus.begin_fill()
    polygon(zeus,10,30)
    zeus.end_fill()
















    















