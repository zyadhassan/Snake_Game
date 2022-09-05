from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.load_score() # update v1.1
        self.penup()
        self.color("white")
        self.goto(x=0,y=265)
        self.score = 0
        self.write(f"Score : {self.score}   High Score = {self.high_score} ", align='center', font=('Courier', 24, 'normal'))

    def increase(self):
        self.score+=1
        self.update()
# Upadat on v1.1
    def reset_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0
        self.save_score()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER. ", align='center', font=('Courier', 36, 'normal'))
 # update on v1.1
    def update(self):
        self.clear()
        self.write(f"Score : {self.score}   High Score = {self.high_score} ", align='center', font=('Courier', 24, 'normal'))

    def save_score(self):
        with open("High_Score.txt",mode="w") as file:
            file.write(str(self.high_score))

    def load_score(self):
        with open("High_Score.txt") as file:
            self.high_score = int (file.read())
