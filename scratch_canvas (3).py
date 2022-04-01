import turtle
import random

dict_1 = {'Shape1': 'square', 'Shape2': 'triangle', 'Shape3': 'circle'}
colors = ['orange', 'red', 'green', 'blue', 'yellow']

user_input = input('Enter the shape you desire to draw')

turtle.fillcolor(random.choice (colors))

turtle.beginfill()

if dict_1.get('Shape1')==user_input:
    for i in range (4):
        turtle.fd(100)
        turtle.left(90)
    
elif dict_1.get('Shape2')==user_input:
    for i in range (3):
        turtle.fd(100)
        turtle.left(120)

elif dict_1.get('Shape3')==user_input:
    turtle.circle(100)

else:
    print('Enter a value between square, triangle and circle')

turtle.endfill()






























