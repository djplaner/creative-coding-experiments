"""
sierpinski.py

- Simple implementation of Sierpinski's triangle using p5
"""

from p5 import *
from random import choice as random_choice, uniform as random_uniform

screenWidth = 1000
screenHeight = 800

triangleWidth = screenWidth - 50
triangleHeight = screenHeight - 50

circleSize = 5

def setup():
    size(screenWidth, screenHeight) 
    background(255)
    no_stroke()
    
    
def draw():
    
    # draw a filled circle at point 0,0 diameter 10
    fill(123, 15)

    # define coords of three verticies of triangle
    width = triangleWidth
    height = triangleHeight
    vertices = [(width/2, 10), (width, 10+height), (70, 10+height)]

    # display a circle at each vertex
    for vertex in vertices:
        circle(vertex, circleSize)

    # randomly choose x between 70 and width
    # randomly choose y between 10 and height
    currentPoint = ( random_uniform(70, width), random_uniform(10, height) )
    #circle(currentPoint, circleSize*10)

    #print(currentPoint)

    # 2000 times
    for i in range(2000):
        # pick a random vertex
        v = random_choice(vertices)
        # pick a random colour 
        fill(random_uniform(0,255), random_uniform(0,127), random_uniform(0,51), 127)
        # calculate a point halfway between the current point and the random vertex
        x = (currentPoint[0] + v[0]) / 2
        y = (currentPoint[1] + v[1]) / 2
        currentPoint = (x, y)
        circle(currentPoint,circleSize)

    #input("checking")

    
run(renderer="vispy")