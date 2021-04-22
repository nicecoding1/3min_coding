import random
import turtle
from tkinter import *

# r,g,b 색상 만들어 반환하는 함수
def getRGB():
    r, g, b = 0, 0, 0
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)


# x,y 좌표 만들어 반환하는 함수
def getXY(sw, sh):
    x, y =0, 0
    x = random.randrange(-sw/2, sw/2)
    y = random.randrange(-sh/2, sh/2)
    return x, y


win = Tk()
win.title("Turtle Canvs")

drw = Canvas(win, width=500, height=500)
drw.pack()

t = turtle.RawTurtle(drw)
t.shape("turtle")
sc_w = 400
sc_h = 400

for i in range(30):
    tX, tY = getXY(sc_w, sc_h)
    r, g, b = getRGB()
    radius = random.randrange(20, 80)
    t.begin_fill()
    t.color(r, g, b)

    # 별 그리는 부분
    for i in range(5):
        t.forward(radius)
        t.right(144)

    t.end_fill()
    t.penup()
    t.goto(tX, tY)
    t.pendown()

win.mainloop()
