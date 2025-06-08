from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.points}", align="center", font=('Arial', 15, 'normal'))

    def give_point(self):
        self.clear()
        self.points += 1
        self.write(f"Score: {self.points}", align="center", font=('Arial', 20, 'normal'))


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=('Arial', 15, 'normal'))
