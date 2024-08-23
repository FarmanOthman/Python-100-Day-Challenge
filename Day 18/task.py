import turtle
t = turtle.Turtle()

t.shape("turtle")

for j in range(4,11,1):
  for i in range(1,j,1):
    t.forward(60)
    t.right(360/(j-1))

turtle.done()