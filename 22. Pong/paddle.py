from turtle import Turtle

class Paddle(Turtle):
        
        def __init__(self, position):
            super().__init__()
            self.penup()
            self.shape("square")
            self.shapesize(stretch_len=1, stretch_wid=5)
            self.color("white")
            self.goto(position)

        def goUp(self):
            if self.ycor() < 260:
                newY = self.ycor() + 20
                self.goto(self.xcor(), newY)

        def goDown(self):
            if self.ycor() > -260:
                newY = self.ycor() - 20
                self.goto(self.xcor(), newY)
