'''
pip install freegames
'''
from freegames import square, vector  
from random import randrange
from turtle import *

#vector(x,y)
snake = [vector(10, 0)]
mouse = vector(0, 0)
aim = vector(10, 0)

def checkInbound(head):
    return  -200 < head.y < 190 and -200 < head.x < 190

def switchDirection(x, y):
    aim.x = x
    aim.y = y

def move():
    head = snake[-1].copy()
    head.move(aim)

    if not checkInbound(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == mouse:
        print('Snake size:', len(snake))
        #update new random mouse location
        mouse.x = randrange(-18, 18) * 10
        mouse.y = randrange(-18, 18) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')
    
    #create new mouse with random location 
    square(mouse.x, mouse.y, 9, 'blue')
    #refresh screen with new mouse location
    update()
    #call move() after 100 milliseconds
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: switchDirection(0, 10), 'Up')
onkey(lambda: switchDirection(0, -10), 'Down')
onkey(lambda: switchDirection(10, 0), 'Right')
onkey(lambda: switchDirection(-10, 0), 'Left')
move()
done()