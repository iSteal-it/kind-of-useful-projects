from turtle import Turtle
import random

class Ball():
    def __init__(self):
        self.ball = Turtle()
        self.ball.shape('circle')
        self.ball.color('white')
        self.ball.penup()
        self.speed = 5
        self.ball.setheading(random.randint(20,160))

    def go(self):
        self.ball.fd(self.speed)

    def chk(self):
        xball = self.ball.xcor()
        yball = self.ball.ycor()
        if xball >= 380:
            heading = self.ball.heading()
            self.ball.setheading(180 - heading)

        if xball <= -380:
            heading = self.ball.heading()
            self.ball.setheading(180 - heading)

        if yball >= 380:
            heading = self.ball.heading()
            self.ball.setheading(-heading)



