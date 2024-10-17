# 'turtle' is a built-in graphics program for Python.
# We are drawing using the 'turtle' library today!
# First, we need to import the turtle library. Then, we must initialize the screen and turtle objects. Finally, we set the turtle's speed to 1, so we can see what is happening.
import turtle
screen = turtle.Screen()
screen.setup(width=500, height=500)
t = turtle.Turtle()
t.pensize(3)
t.speed(1)


# The next few lines draw a box:
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

# Run the program now. You'll need to move your code window to see the turtle window. You should see a black square.

turtle.done()


# That was a lot of typing for one square. Let's see how we can use loops to draw our square instead:

t.color("RED")
t.pensize(8)
for side in range(4):
    t.forward(100)
    t.right(90)

# that's a lot less code, right? To see this in action, comment out the turtle.done() line on line 24, then run the program. The thick, red line is the hexagon made using the loop.

turtle.done()


