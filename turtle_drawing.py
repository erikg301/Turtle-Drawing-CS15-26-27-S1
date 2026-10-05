import turtle

screen = turtle.Screen()
screen.title("Erik")

t = turtle.Turtle()
t.speed(3)
t.pensize(6)
t.hideturtle()

square = 40
gap = 25
diagonal = square * 2 ** 0.5

# Letters are 1 square wide and 2 squares tall.
# Every letter starts at its bottom-left corner facing east
# and finishes at its bottom-right corner facing east.

# Move to the start: back up half the total width, then down half the height
t.penup()
total_width = (square * 4) + (gap * 3)
t.backward(total_width / 2)
t.right(90)
t.forward(square)
t.left(90)

# E
t.color("red")
t.pendown()
t.left(90)
t.forward(square * 2)       # up the left side
t.right(90)
t.forward(square)           # top bar
t.backward(square)
t.right(90)
t.forward(square)           # down to the middle
t.left(90)
t.forward(square)           # middle bar
t.backward(square)
t.right(90)
t.forward(square)           # down to the bottom
t.left(90)
t.forward(square)           # bottom bar
t.penup()
t.forward(gap)

# r
t.color("blue")
t.pendown()
t.left(90)
t.forward(square * 2)       # up the left side
t.right(90)
t.forward(square)           # top bar
t.right(90)
t.forward(square)           # down the right side of the bowl
t.right(90)
t.forward(square)           # middle bar back to the stem
t.left(135)
t.forward(diagonal)         # diagonal leg
t.left(45)
t.penup()
t.forward(gap)

# i
t.color("green")
t.pendown()
t.forward(square)           # bottom bar
t.backward(square / 2)
t.left(90)
t.forward(square * 2)       # up the middle
t.left(90)
t.forward(square / 2)       # top bar (left half)
t.backward(square)          # top bar (right half)
t.penup()
t.left(90)
t.forward(square * 2)       # back down to the bottom-right corner
t.left(90)
t.forward(gap)

# k
t.color("purple")
t.pendown()
t.left(90)
t.forward(square * 2)       # up the stem
t.backward(square)          # back to the middle
t.right(45)
t.forward(diagonal)         # up-right arm
t.backward(diagonal)
t.right(90)
t.forward(diagonal)         # down-right leg
t.left(45)
t.penup()

screen.exitonclick()

