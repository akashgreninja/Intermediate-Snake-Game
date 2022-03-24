
from turtle import  Turtle
ALIGNMENT="center"
FONT=("Courier", 18, "normal",)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()


        self.score=0
        self.high=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
        # self.high_score()


    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)

        self.write(f"SCORE ={self.score}  High score={self.high}",  align=ALIGNMENT, font=FONT)

    # def high_score(self):
    #
    #     self.goto(-200, 270)
    #     self.write(f"", align=ALIGNMENT, font=FONT)


    def restart(self):
        if self.score >self.high:
            self.high=self.score
        self.score=0
        self.update_scoreboard()



    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)



    def increasescore(self):

        self.score+=1

        self.update_scoreboard()
        # self.high_score()


    #
    # def restart(self):
    #     self.game_over()