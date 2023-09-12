from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ascore = 0

    def score(self):
        self.ht()
        self.setposition(0, 270)
        self.penup()
        self.color("white")
        self.write(f"Score: {self.ascore}", True, "center", ("Courier", 15, "normal"))
    
    def gameover(self):
        self.ht()
        self.setposition(0, 0)
        self.penup()
        self.color("white")
        self.write(f"Game Over.", True, "center", ("Courier", 15, "normal"))

    def increase_score(self):
        self.clear()
        self.ascore += 1
        self.score() 

