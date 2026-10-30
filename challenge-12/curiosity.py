"""Draw cutout boundaries. Use matching SVG overlay for true transparency."""
import turtle as t
t.setup(800,850)
t.speed(5)
t.shape("turtle")
t.pencolor('#416b7c')
t.ht()
t.penup()
t.goto(-383, 408)
t.st()
t.pendown()
for x,y in [(383, 408), (383, -408), (-383, -408), (-383, 408)]:
    t.goto(x,y)
t.ht()
t.penup()
t.goto(-345, 190)
t.st()
t.pendown()
for x,y in [(360, 190), (360, -310), (-345, -310), (-345, 190)]:
    t.goto(x,y)
t.ht()
t.penup()
