import turtle as tur
import colorsys as cs

def draw():
    tur.setup(800,800)
    tur.speed(0)
    tur.tracer(10)
    tur.width(2)
    tur.bgcolor("black")

    for j in range(25):
        for i in range(15):
            # set color using hsv values
            tur.color(cs.hsv_to_rgb(i/15,j/25,1))

            #draw right arc
            tur.right(90)
            tur.circle(200-j*4,90)

            #draw left arc
            tur.left(90)
            tur.circle(200-j*4,90)

            # reverse direction to connect the circle
            tur.right(180)
            tur.circle(50,24)
    tur.hideturtle()

draw()
tur.done()