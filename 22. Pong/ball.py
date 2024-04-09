from turtle import Turtle

class ballMovement(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("white")
        self.penup()
        self.xMove = 10
        self.yMove = 10

    def move(self):
        newX = self.xcor() + self.xMove
        newY = self.ycor() + self.yMove
        self.goto(newX, newY)
   
    def bounce(self):
        self.yMove *= -1
        
    def hit(self):
        self.xMove *= -1

    def resetPosition(self):
        self.goto(0,0)
        self.hit()
