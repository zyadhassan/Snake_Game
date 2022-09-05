from Snake import Snake
import time
from Food import Food
from scoreboard import ScoreBoard
SCREEN_W=600
SCREEN_H=600

# Setup the Screen window
from turtle import Screen

screen = Screen()
screen.setup(width=SCREEN_W, height=SCREEN_H) # Window Size 600*600
screen.bgcolor("black")  # the background is black
screen.title("Snake Game v1.1")  # the title of the window
screen.tracer(0)



s1=Snake(length=3)
food=Food()
score=ScoreBoard()


# Screen Events
screen.listen()
screen.onkey(s1.up,"Up")
screen.onkey(s1.down,"Down")
screen.onkey(s1.right,"Right")
screen.onkey(s1.left,"Left")




# Game ON
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    s1.move()
    if(s1.head.distance(food)<20):
        s1.eat()
        food.change()
        score.increase()
    if s1.collision_wall(width=SCREEN_W,height=SCREEN_H) or s1.collision_tail():
       # update V1.1
        s1.reset()
        score.reset()
        screen.update()
        time.sleep(0.7)




# To keep window open

screen.exitonclick()
