import turtle

ground = turtle.Screen()
ground.bgpic("ground.png")
ground.addshape("left.gif")
ground.addshape("right.gif")
ground.addshape("ball.gif")
rightplayer= turtle.Turtle()
rightplayer.penup()
rightplayer.shape("right.gif")
rightplayer.goto(400,-200)

leftplayer = turtle.Turtle()
leftplayer.penup()
leftplayer.shape("left.gif")
leftplayer.goto(-400,200)

leftpen =turtle.Turtle()
leftpen.penup()
leftpen.hideturtle()
leftpen.goto(-400,250)
leftpen.color("white")
leftpen.write("Leftplayer Score:0",font=("Courier",27,"bold"))

rightpen =turtle.Turtle()
rightpen.penup()
rightpen.hideturtle()
rightpen.goto(100,250)
rightpen.color("white")
rightpen.write("rightplayer Score:0",font=("Courier",27,"bold"))

ball=turtle.Turtle()
ball.penup()
ball.shape("ball.gif")

def leftplayerup():
    y=leftplayer.ycor()
    leftplayer.sety(y+10)
def leftplayerdown():
    y= leftplayer.ycor()
    leftplayer.sety(y-10)
def leftplayerright():
    x= leftplayer.xcor()
    leftplayer.setx(x+10)
def leftplayerleft():
    x=leftplayer.xcor()
    leftplayer.setx(x-10)
def rightplayerup():
    y=rightplayer.ycor()
    rightplayer.sety(y+10)
def rightplayerdown():
    y=rightplayer.ycor()
    rightplayer.sety(y-10)
def rightplayerright():
    x= rightplayer.xcor()
    rightplayer.setx(x+10)
def rightplayerleft():
    x= rightplayer.xcor()
    rightplayer.setx(x-10)

turtle.onkeypress(leftplayerup,"w")
turtle.onkeypress(leftplayerdown,"s")
turtle.onkeypress(leftplayerright,"d")
turtle.onkeypress(leftplayerleft,"a")

turtle.onkeypress(rightplayerup,"Up")
turtle.onkeypress(rightplayerdown,"Down")
turtle.onkeypress(rightplayerleft,"Left")
turtle.onkeypress(rightplayerright,"Right")

turtle.listen()
dx=5
dy=-5
leftscore=0
rightscore=0
while True:
    x=ball.xcor()
    y= ball.ycor()
    ball.setpos(x+dx,y-dy)
    if rightplayer.distance(ball)<10 or leftplayer.distance(ball)<10:
        dx=-dx
    if ball.ycor()<-280 or ball.ycor()>280:
        dy=-dy
    if ball.xcor()>450 :
        ball.goto(0,0)
        leftpen.clear()
        leftscore=leftscore+1
        leftpen.write(("Leftplayer Score:{}").format(leftscore),font=("Courier",27,"bold"))
    if ball.xcor()<-450:
        ball.goto(0,0)
        rightpen.clear()
        rightscore=rightscore+1
        rightpen.write(("Rightplayer Score:{}").format(rightscore),font=("Courier",27,"bold"))

turtle.done()