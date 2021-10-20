from turtle import Turtle


class Paddle():
    def __init__(self):
        self.paddle = Turtle()
        self.paddle.color('cornflower blue')
        self.paddle.shape('square')
        self.paddle.shapesize(stretch_len=6)
        self.paddle.penup()
        self.paddle.goto(x=0, y=-320)

    def goright(self):
        if self.paddle.xcor() <= 320:
            self.paddle.goto(x=self.paddle.xcor() + 10,y=self.paddle.ycor())

    def goleft(self):
        if self.paddle.xcor() >= -330:
            self.paddle.goto(x=self.paddle.xcor() - 10, y=self.paddle.ycor())