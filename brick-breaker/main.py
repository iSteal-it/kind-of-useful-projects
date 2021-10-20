from turtle import *
from paddle import Paddle
from ball import Ball

game = True

paddle = Paddle()
ball = Ball()


screen = Screen()
screen.bgcolor('black')
screen.title('Brick Breaker')
screen.setup(width=800,height=800)

while game:
    ball.go()
    ball.chk()
    onkey(paddle.goleft, "Left")
    onkey(paddle.goright, "Right")
    screen.listen()

screen.exitonclick()