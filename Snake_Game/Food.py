from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.speed(15)
        self.x=random.randint(-280,280)
        self.y = random.randint(-280, 280)
        self.goto(self.x,self.y)

    def change(self):
        self.x = random.randint(-280, 280)
        self.y = random.randint(-280, 280)
        self.goto(self.x, self.y)