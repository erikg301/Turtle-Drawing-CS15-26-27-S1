import turtle as t
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)

t.reset()
square = 30
gap = 10
t.penup()

# Account for 'H' and 'e' and the gaps between them
backward_length = (square * 2) + (gap * 2)

t.backward(backward_length)

# H
t.pendown()
t.left(90)
t.forward(square * 2)
t.backward(square)
t.right(90)
t.forward(square)
t.left(90)
t.forward(square)
t.backward(square * 2)
t.right(90)
t.penup()
t.forward(gap)

# e
t.pendown()
t.left(90)
t.forward(square)
t.right(90)
t.forward(square)
t.right(90)
t.forward(square / 2)
t.right(90)
t.forward(square)
t.left(90)
t.forward(square / 2)
t.left(90)
t.forward(square)
t.penup()
t.forward(gap)

# l
t.pendown()
t.left(90)
t.forward(square * 2)
t.right(90)
t.penup()
t.forward(gap)

# l
t.pendown()
t.right(90)
t.forward(square * 2)
t.left(90)
t.penup()
t.forward(gap)

# o
t.pendown()
t.forward(square)
t.left(90)
t.forward(square)
t.left(90)
t.forward(square)
t.left(90)
t.forward(square)