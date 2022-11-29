import turtle
import tkinter
import time
import math


class Sprite(turtle.Turtle):

    def __init__(self, x, y, shape, health=0):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.health = health
        self.setx(x)
        self.sety(y)
        self.center = [x, y]
        turtle.register_shape(shape)
        self.shape(shape)
        self.showturtle()
        self.height = 0
        self.width = 0
        self.dy = 0
        self.ready = True
        self.destroyed = False

    def set_bounding_circle(self, height, width):
        self.center = [self.xcor(), self.ycor()]
        self.height = height
        self.width = width
        return

    def angle(self, other):
        if (self.xcor()-other.xcor() == 0):
            return math.pi/2
        else:
            theta = math.atan(self.ycor()-other.ycor()) / \
                (self.xcor()-other.xcor())
            return theta

    def collisions(self, other):
        # returns bool
        distance = self.get_distance(other)
        xdistance = distance*math.cos(self.angle(other))
        ydistance = distance*math.sin(self.angle(other))
        hit = xdistance < (self.width/2 + other.width /
                           2) and ydistance < (self.height/2 + other.height/2)
        if hit:
            self.ready = True
        return hit

    def get_distance(self, other):
        return math.sqrt((self.ycor()-other.ycor())**2+(self.xcor()-other.xcor())**2)

    def destroy_actor(self):
        self.hideturtle()
        self.destoyed = True
        return

    def jump(self):
        if self.ready:
            self.dy += 12
            self.ready = False
        return
