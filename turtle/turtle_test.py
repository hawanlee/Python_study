import turtle

window = turtle.Screen()

t = turtle.Turtle()
t.shape('turtle')
for i in range(60):
    t.speed(1)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.circle(50)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.right(6)

# p = turtle.Turtle()
# p.color('red')
# p.circle(150)

window.exitonclick()