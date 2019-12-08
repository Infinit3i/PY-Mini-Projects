# created by Matthew Iverson 
# www.matthewiver.com

import turtle

wn = turtle.Screen()
wn.title("Pong by Matthew Iverson")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score_one = 0
score_two = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player One: {} Player Two: {}".format(score_one, score_two), align="center", font=("Courier", 24, "normal"))

paddle_one = turtle.Turtle()
paddle_one.speed(0)
paddle_one.shape("square")
paddle_one.color("purple")
paddle_one.shapesize(stretch_wid=5, stretch_len=1)
paddle_one.penup()
paddle_one.goto(-350, 0)

paddle_two = turtle.Turtle()
paddle_two.speed(0)
paddle_two.shape("square")
paddle_two.color("red")
paddle_two.shapesize(stretch_wid=5, stretch_len=1)
paddle_two.penup()
paddle_two.goto(350, 0)

game_ball = turtle.Turtle()
game_ball.speed(0)
game_ball.shape("square")
game_ball.color("white")
game_ball.penup()
game_ball.goto(0, 0)
game_ball.dx = .25
game_ball.dy = .25

def paddle_one_up():
    y = paddle_one.ycor()
    y += 20
    paddle_one.sety(y)

def paddle_one_down():
    y = paddle_one.ycor()
    y -= 20
    paddle_one.sety(y)

def paddle_two_up():
    y = paddle_two.ycor()
    y += 20
    paddle_two.sety(y)

def paddle_two_down():
    y = paddle_two.ycor()
    y -= 20
    paddle_two.sety(y)

wn.listen()
wn.onkeypress(paddle_one_up, "w")
wn.onkeypress(paddle_one_down, "s")
wn.onkeypress(paddle_two_up, "Up")
wn.onkeypress(paddle_two_down, "Down")

# Main game loop
while True:
    wn.update()

    game_ball.setx(game_ball.xcor() + game_ball.dx)
    game_ball.sety(game_ball.ycor() + game_ball.dy)

    if game_ball.ycor() > 290:
        game_ball.sety(290)
        game_ball.dy *= -1
    
    if game_ball.ycor() < -290:
        game_ball.sety(-290)
        game_ball.dy *= -1

    if game_ball.xcor() > 390:
        game_ball.goto(0, 0)
        game_ball.dx *= -1
        score_one += 1
        pen.clear()
        pen.write("Player One: {} Player Two: {}".format(score_one, score_two), align="center", font=("Courier", 24, "normal"))

    if game_ball.xcor() < -390:
        game_ball.goto(0, 0)
        game_ball.dx *= -1
        score_two += 1
        pen.clear()
        pen.write("Player One: {} Player Two: {}".format(score_one, score_two), align="center", font=("Courier", 24, "normal"))

    if game_ball.xcor() > 330 and game_ball.xcor() < 350 and (game_ball.ycor() < paddle_two.ycor() + 40 and game_ball.ycor() > paddle_two.ycor() - 40):
       game_ball.setx(330)
       game_ball.dx *= -1 

    if game_ball.xcor() < -330 and game_ball.xcor() < 350 and (game_ball.ycor() < paddle_one.ycor() + 40 and game_ball.ycor() > paddle_one.ycor() - 40):
       game_ball.setx(-330)
       game_ball.dx *= -1 