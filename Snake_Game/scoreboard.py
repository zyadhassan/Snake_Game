from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.high_score=0 # update v1.1
        self.penup()
        self.color("white")
        self.goto(x=0,y=265)
        self.score = 0
        self.write(f"Score : {self.score}   High Score = {self.high_score} ", align='center', font=('Courier', 24, 'normal'))

    def increase(self):
        self.score+=1
        self.update()
# Upadat on v1.1
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER. ", align='center', font=('Courier', 36, 'normal'))
 # update on v1.1
    def update(self):
        self.clear()
        self.write(f"Score : {self.score}   High Score = {self.high_score} ", align='center', font=('Courier', 24, 'normal'))
