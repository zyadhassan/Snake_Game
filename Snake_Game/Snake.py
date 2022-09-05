from turtle import Turtle


class Snake:
    def __init__(self,length):
        self.segmants=[]
        ############ Creating the Snack ################
        for i in range(length):
            turt = Turtle()
            turt.color("white")
            turt.shape("square")
            turt.penup()
            turt.setposition(x=0 - (20 * i), y=0)
            self.segmants.append(turt)

        #############################################

        self.length=length
        self.head=self.segmants[0]

    def move(self):
        for i in range(self.length - 1, 0, -1):
            self.segmants[i].goto(self.segmants[i - 1].xcor(), self.segmants[i - 1].ycor())
        self.head.fd(20)

    def up(self):
        if(self.head.heading()!=270):
            self.head.setheading(90)
            self.move()

    def down(self):

        if(self.head.heading()!=90):
            self.head.setheading(270)
            self.move()
    def right(self):
        if (self.head.heading() != 180):
            self.head.setheading(0)
            self.move()
    def left(self):
        if (self.head.heading() != 0):
            self.head.setheading(180)
            self.move()

    def eat(self):

        turt = Turtle()
        turt.color("white")
        turt.shape("square")
        turt.penup()
        turt.setposition(x=self.segmants[self.length-1].xcor(), y=self.segmants[self.length-1].ycor())
        self.length += 1
        self.segmants.append(turt)

    def collision_wall(self,width,height):
        mid_w=width/2
        mid_h=height/2

        if self.head.xcor()>mid_w-15 or self.head.xcor()<-mid_w+15 :
            return True
        elif self.head.ycor() > mid_h-15 or self.head.ycor() < -mid_h+15:
            return True
        else:
            return False

    def collision_tail(self):
        for i in range(1,self.length):
            distance=self.head.distance(self.segmants[i])
            if distance<10 :
                return True

        return False
# Update V1.1
    def reset(self):
        for seg in self.segmants:
            seg.setposition(650,650)
        for i in range(3):
            self.segmants[i].setposition(x=0 - (20 * i), y=0)
        self.length = 3
        self.head = self.segmants[0]
        self.segmants=self.segmants[:3]













