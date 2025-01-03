from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 12, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg=f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)

        self.write(arg=f'GAME OVER!', move=False, align=ALIGNMENT, font=("Courier", 24, 'bold'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
