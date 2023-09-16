

from turtle import *

 

a = Turtle()
a.speed(300)
for i in range(100) :
    a.circle(100)
    a.left(90)    
    a.left(180)
    a.left(180)
    a.right(90)
    for i in range(10) :
        a.forward(5)
        a.left(5)
a.getscreen()._root.mainloop()
