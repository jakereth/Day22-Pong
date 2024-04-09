from turtle import Screen, Turtle


class Score(Turtle):

    def __init__ (self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player1Score = 0
        self.player2Score = 0
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player1Score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.player2Score, align="center", font=("Courier", 80, "normal"))

    def addScore_Player1(self):
        self.player1Score += 1
        self.updateScoreboard()

    def addScore_Player2(self):
        self.player2Score += 1
        self.updateScoreboard()

