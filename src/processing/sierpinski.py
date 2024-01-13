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

circleSize = 25

def setup():
    size(screenWidth, screenHeight) 
    background(255)
    no_stroke()
    
    
def draw():
    
    # draw a filled circle at point 0,0 diameter 10
    fill(123, 15)

    # define coords of three verticies of triangle
    vertices = [(triangleWidth/2, circleSize+5), (triangleWidth, 10+triangleHeight), (70, 10+triangleHeight)]

    # display a circle at each vertex
    for vertex in vertices:
        circle(vertex, circleSize)

    #-- get a starting point along the base line of the triangle
    # - making certain it's in the triangle
    currentPoint = ( random_uniform(70, triangleWidth), random_uniform(triangleHeight, 10+triangleHeight) )
    #circle(currentPoint, circleSize*100)
    stroke(0)

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


if __name__ == "__main__": 
    run(renderer="vispy")