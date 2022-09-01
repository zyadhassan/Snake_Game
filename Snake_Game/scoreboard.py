from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0,y=265)
        self.score = 0
        self.write(f"Score : {self.score} ", align='center', font=('Courier', 24, 'normal'))

    def increase(self):
        self.score+=1
        self.clear()
        self.write(f"Score : {self.score} ", align='center', font=('Courier', 24, 'normal'))


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER. ", align='center', font=('Courier', 36, 'normal'))