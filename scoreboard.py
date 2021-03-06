
from turtle import  Turtle
ALIGNMENT="center"
FONT=("Courier", 24, "normal",)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()


        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)

        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"SCORE ={self.score}",  align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)



    def increasescore(self):
        self.clear()
        self.score+=1

        self.update_scoreboard()


