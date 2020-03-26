import turtle
import random
import time


def player1():
    p1 = turtle.Turtle()
    p1.pu()
    p1.speed(0)
    p1.seth(90)
    p1.setx(-250)
    p1.shape('square')
    p1.shapesize(stretch_wid=.75, stretch_len=4)
    p1.color('white')
    return p1


def player2():
    p2 = turtle.Turtle()
    p2.pu()
    p2.speed(0)
    p2.seth(90)
    p2.setx(250)
    p2.shape('square')
    p2.shapesize(stretch_wid=.75, stretch_len=4)
    p2.color('white')
    return p2


def board():
    t1 = turtle.Turtle()
    t1.ht()
    t1.pu()
    t1.pensize(4)
    t1.color('white')
    t1.speed(0)
    return t1


def pauseturtle():
    t3 = turtle.Turtle()
    t3.ht()
    t3.pu()
    t3.pensize(7)
    t3.color('white')
    t3.speed(0)
    t3.seth(-90)
    return t3


def winturtle():
    w = turtle.Turtle()
    w.ht()
    w.pu()
    w.color('white')
    w.speed(0)
    w.ht()
    return w


def ball():
    b = turtle.Turtle()
    b.shape("circle")
    b.speed(0)
    b.color('white')
    return b


def game():
    t2 = turtle.Turtle()
    t2.ht()
    t2.pu()
    t2.color('white')
    t2.pencolor()
    t2.speed(0)
    return t2


def drawboard():
    t1.setpos(-300, 190)
    t1.pd()
    t1.fd(600)
    t1.pu()
    t1.setpos(-300, -190)
    t1.pd()
    t1.fd(600)
    t1.pu()
    t1.setpos(0, 195)
    t1.write("PONG", align="center", font=("Arial", 20, "normal"))
    t1.setpos(-210, -210)
    t1.write("Press Space to Start/Pause", align="center", font=("Arial", 10, "normal"))
    t1.setpos(210, -210)
    t1.write("Press R to Reset Game", align="center", font=("Arial", 10, "normal"))


def playername1():
    p1name = raw_input("Player 1 Name: ")
    p1name = p1name.capitalize()
    return p1name


def playername2():
    p2name = raw_input("Player 2 Name: ")
    p2name = p2name.capitalize()
    return p2name


def moveball(y, a):

    if -180 < y < 180:
        b.fd(5)
    else:
        b.seth(-a)
        if y > 180:
            b.sety(178)
        elif y < -180:
            b.sety(-178)


def gamestatus(n1, n2):
    t2.clear()
    t2.penup()
    score1 = str(str(n1) + ": " + str(p1score))
    score2 = str(str(n2) + ": " + str(p2score))
    t2.goto(-250, 195)
    t2.write(score1, align="center", font=("Arial", 20, "normal"))
    t2.goto(250, 195)
    t2.write(score2, align="center", font=("Arial", 20, "normal"))


def checkcollision(y1, y2, x, y, a):

    if y1 + 45 > y > y1 - 45 and -236 > x > -254:
        b.seth(180-a)
        b.setx(-236)

    elif y2 + 45 > y > y2 - 45 and 236 < x < 254:
        b.seth(180-a)
        b.setx(236)


def up1():
    if -150 < p1.ycor() + 15 < 150:
        p1.fd(15)


def down1():
    if -150 < p1.ycor() - 15 < 150:
        p1.back(15)


def up2():
    if -150 < p2.ycor() + 15 < 150:
        p2.fd(15)


def down2():
    if -150 < p2.ycor() - 15 < 150:
        p2.back(15)


def pause():
    global playing
    if playing:
        playing = False
        t3.setpos(-10, 20)
        t3.pd()
        t3.fd(40)
        t3.pu()
        t3.setpos(10, 20)
        t3.pd()
        t3.fd(40)
        t3.pu()

    elif not playing:
        playing = True
        t3.clear()


def reset():
    global playing
    global p1score
    global p2score
    p1score = 0
    p2score = 0
    playing = False
    b.setpos(0, 0)


def maingame():
    global initial
    global playing
    global p1score
    global p2score
    global name1
    global name2
    while True:
        print playing
        x = b.xcor()
        while -290 < x < 290 and playing:
            b.st()
            w.clear()
            x = b.xcor()
            y = b.ycor()
            a = b.heading()
            y1 = p1.ycor()
            y2 = p2.ycor()
            moveball(y, a)
            checkcollision(y1, y2, x, y, a)
            s.update()
            time.sleep(.03)

        else:
            if x > 290:
                p1score += 1
                playing = False
                b.ht()
                b.setpos(0, 0)
                b.st()
                initial = random.randint(-50, 50)
                b.seth(initial)

            elif x < -290:
                p2score += 1
                playing = False
                b.ht()
                b.setpos(0, 0)
                b.st()
                initial = random.randint(130, 230)
                b.seth(initial)

            if p1score == 10:
                playing = False
                win = str(name1 + " Wins!")
                b.ht()
                b.setpos(0, 0)
                w.write(win, align="center", font=("Arial", 20, "normal"))
                p1score = 0
                p2score = 0
                initial = random.randint(-50, 50)
                b.seth(initial)

            elif p2score == 10:
                playing = False
                win = str(name2 + " Wins!")
                b.ht()
                b.setpos(0, 0)
                w.write(win, align="center", font=("Arial", 30, "normal"))
                p1score = 0
                p2score = 0
                initial = random.randint(-50, 50)
                b.seth(initial)

        gamestatus(name1, name2)
        s.update()
        time.sleep(.04)


p1score = 0
p2score = 0
playing = False

p1 = player1()
p2 = player2()
b = ball()
t1 = board()
t2 = game()
t3 = pauseturtle()
w = winturtle()


initial = random.randint(-50, 50)
b.seth(initial)
b.pu()

name1 = str(playername1())
name2 = str(playername2())


s = turtle.Screen()
s.tracer(0)
s.bgcolor('black')
s.setup(width=600, height=450)


s.onkey(reset, 'r')
s.onkey(pause, 'space')
s.onkey(up2, 'Up')
s.onkey(down2, 'Down')
s.onkey(up1, 'w')
s.onkey(down1, 's')
s.listen()


drawboard()
maingame()


turtle.mainloop()