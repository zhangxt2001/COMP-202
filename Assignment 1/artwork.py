# Name : Xiaoteng Zhang
# McGill ID : 260895923
import turtle

def tangent_circle(num_of_circle, start_radius):
    '''(int,int) -> NoneType (doesn't return anything only drawing on the canvas)
    This function would create tangent circles with the next circle's radius
    being 10 units bigger than the previous one and user can change the number of
    circles desired as well as the starting radius of the circle
    '''
    for i in range(num_of_circle):
        turtle.circle(start_radius+10*i)

def my_artwork():
    ''' () -> ... 
    This function does not require any input
    The purpose of this function is to create three different shapes on canvas along with
    my signature (the first letter of my first name: X)
    1. First block creates two isoceles triangles that share a vertex which are coloured in
    red
    2. Second block creates my signature X. That is located at the very right of the canvas
    3. Third block creates a star. This is located left of the two isoceles triangles. This
    one is coloured in yellow
    4. The final block creates three tangent circles using the first function that I defined
    above
    '''
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.right(60)
    for i in range(2):
        turtle.forward(100)
        turtle.right(120)
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.end_fill()
    turtle.left(60)
    
    turtle.penup()
    turtle.goto(100,50)
    turtle.pendown()
    turtle.right(25)
    turtle.forward(100)
    turtle.penup()
    turtle.goto(170,60)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(100)
    turtle.left(115)
    
    turtle.penup()
    turtle.goto(-200,0)
    turtle.pendown()
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(50)
        turtle.left(144)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(-300,0)
    turtle.pendown()
    tangent_circle(num_of_circle = 3, start_radius = 20)
    