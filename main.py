import domino

a = domino.DominoLine('/||////\\\\\\\||/|||\|||\\\\')
print(a)
a.step_backward(2)
a.step_forward(2)
a.step_forward()
a.step_forward(10)

b = domino.DominoLine('/')
b.step_backward(3)
b.step_forward()

c = domino.DominoLine('?')
