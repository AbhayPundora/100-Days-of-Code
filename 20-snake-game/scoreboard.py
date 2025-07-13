from  turtle import  Turtle
ALIGNMENT = "center"
FONT = ("Arial", 17, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.show_score()


    def increase_score(self):
        self.score += 1

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)


