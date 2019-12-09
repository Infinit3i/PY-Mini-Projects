# Space Invaders
# Created by Matthew Iverson
# www.matthewiver.com
import turtle
import os
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")


border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pensize(3)
border_pen.pendown()
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
    border_pen.hideturtle()

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250) 
player.setheading(90)

playerspeed = 15

number_of_enemies = 5
enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy = turtle.Turtle()
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(-200, 250)

enemyspeed = 2

laser = turtle.Turtle()
laser.shapesize(0.5, 0.5)
laser.setheading(90)
laser.color("yellow")
laser.shape("triangle")
laser.penup()
laser.speed(0)
laser.hideturtle()

laserspeed = 20

laserstate = "ready"


def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = 280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = -280
    player.setx(x)

def fire_laser():
    global laserstate
    if laserstate == "ready":
        laserstate = "fire"
        x = player.xcor()
        y = player.ycor()
        laser.setposition(x, y + 10)
        laser.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(fire_laser, "space")

while True:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280:
            y = enemy.ycor()
            y -= 20
            enemyspeed *= -1
            enemy.sety(y)
        elif enemy.xcor() < -280:
            y = enemy.ycor()
            y -= 20
            enemyspeed *= -1
            enemy.sety(y)

    if laserstate == "fire":
        y = laser.ycor()
        y += laserspeed
        laser.sety(y)

    if laser.ycor() > 275:
        laser.hideturtle()
        laserstate = "ready"

    if isCollision(laser, enemy):
        laser.hideturtle()
        laserstate = "ready"
        laser.setposition(0, -400)
        enemy.setposition(-200, 250)

    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break