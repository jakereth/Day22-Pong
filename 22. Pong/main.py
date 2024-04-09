from turtle import Turtle, Screen
from paddle import Paddle
from ball import ballMovement
from scoreboard import Score
import time

#setup display screen
screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
player1 = Paddle((-350,0))
player2 = Paddle((350,0))
ball = ballMovement()
scoreboard = Score()

#create divider for sides
for i in range(23):
    div = Turtle()
    div.penup()
    div.shape("square")
    div.shapesize(stretch_len=.2, stretch_wid=1)
    div.color("white")
    div.goto(0,600)
    newY = div.ycor() - (50 * i)
    div.goto(0, newY )

#listen for keys that control up and down movement
screen.listen()
screen.onkey(player1.goUp, "w")
screen.onkey(player1.goDown, "s")
screen.onkey(player2.goUp, "Up")
screen.onkey(player2.goDown, "Down")

gameStatus = True
while gameStatus:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #detect vertical collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #detect collision with paddle
    if ball.distance(player2) < 50 and ball.xcor() > 320 or ball.distance(player1) < 50 and ball.xcor() < -320:
        ball.hit() 

    #detect when ball misses paddle
    if ball.xcor() > 380:
        ball.resetPosition()
        scoreboard.addScore_Player1()

    if ball.xcor() < -380:
        ball.resetPosition()
        scoreboard.addScore_Player2()

screen.exitonclick()