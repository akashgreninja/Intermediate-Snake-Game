import random
from  turtle import Turtle

COORDINATE_SYSTEM=[(-20,0),(-40,0),(-60,0)]
RANDOM=["blue","green","red","orange"]

RANDOM_COOR=[(-20,-80),(-40,-67),(-60,-20)]
MOVE_DIST=20
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:
#init is the func you want to call as soon as a class is created
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head=self.all_turtles[0]
#self.move is not created because its a attribute which need not be executed everytime a object is being called
    def create_snake(self):

        for i in COORDINATE_SYSTEM:
            self.add_segment(i)



    def add_segment(self,i):

        timmy = Turtle(shape="square")
        timmy.penup()
        timmy.color("white")
        timmy.goto(i)
        self.all_turtles.append(timmy)

    def extend(self):
        self.add_segment(self.all_turtles[-1].pos())





    def move(self):
        for m in range(len(self.all_turtles) - 1, 0, -1):
            x_cor = self.all_turtles[m - 1].xcor()
            y_cor = self.all_turtles[m - 1].ycor()
            self.all_turtles[m].goto(x_cor, y_cor)
            self.all_turtles[m].color(random.choice(RANDOM))
        self.head.forward(MOVE_DIST)


    def up(self):
        if self.head.heading() !=DOWN:
            self.all_turtles[0].setheading(UP)



    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)



    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)





