def polygon( t ,sides, distance):
    angle = 360 / sides
    #t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.left(angle)
    #t.end_fill()

def circles(t):
    bob.penup()
    bob.goto(-15,0)
    c=(0,times,0)
    bob.forward(0)
    bob.right(45)
    bob.forward(200)
    bob.pendown()
