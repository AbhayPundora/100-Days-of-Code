from  turtle import  Turtle
ALIGNMENT = "center"
FONT = ("Arial", 17, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.show_score()


    def read_high_score(self):
        with open("data.txt") as file:
            data = file.read()
            return int(data)

    def set_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.score))


    def increase_score(self):
        self.score += 1

    def show_score(self):
        self.clear()
        self.high_score = self.read_high_score()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align = ALIGNMENT, font = FONT)
    #


    def reset(self):
        if self.score > self.high_score:
            self.set_high_score()

        self.score = 0
        self.show_score()


