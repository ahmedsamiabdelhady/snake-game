from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high-score.txt") as file:
            self.high_score = int(file.read())
        

    def update_score(self):
        self.clear()
        self.ht()
        self.setposition(0, 270)
        self.penup()
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.high_score}", True, "center", ("Courier", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high-score.txt", mode= "w") as file:
               file.write(str(self.high_score))
        self.score = 0
        self.update_score()

