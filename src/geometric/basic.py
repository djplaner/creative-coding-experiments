"""
basic.py

Manim experiment to re-create some of the basic geometric patterns/algorithms introduced by Artut (2023)


Artut, S. (2023). Geometric Patterns with Creative Coding: Coding for the Arts. Apress. https://doi.org/10.1007/978-1-4842-9389-8

"""

from manim import *

from math import sqrt


class CirclesToHexagon(Scene):
    def construct(self):
        """
        Animate how drawing three circles can be used to create an equal-sided hexagon
        """
        fill = 0
        middleCircle = Circle(radius=1, color=BLUE, fill_opacity=fill)
        leftCircle = Circle(radius=1, color=GREEN, fill_opacity=fill).shift(LEFT)
        rightCircle = Circle(radius=1, color=YELLOW, fill_opacity=fill).shift(RIGHT)
        
        self.play(Create(middleCircle,run_time=1)  )
        self.play(Create(leftCircle,run_time=1)  )
        self.play(Create(rightCircle,run_time=1)  )

        """
        Calculate the x,y coordinates for circles all radius 1 where the left  and middle circles intersect
        """
        leftMiddle = Point(location = [-1,0,0], color=WHITE)
        rightMiddle = Point(location = [1,0,0], color=WHITE)
        leftTop = Point( location=[-0.5, sqrt(3)/2, 0], color=WHITE)
        leftBottom = Point( location=[-0.5, -sqrt(3)/2, 0], color=WHITE)
        rightTop = Point( location=[0.5, sqrt(3)/2, 0], color=WHITE)
        rightBottom = Point( location=[0.5, -sqrt(3)/2, 0], color=WHITE)
        
        self.add(leftMiddle, rightMiddle, leftTop, leftBottom, rightTop, rightBottom)

        self.wait(1)
        #-- draw lines between the points
        leftMiddleLine = Line(leftMiddle, leftTop, color=WHITE)
        topLine = Line(leftTop, rightTop, color=WHITE)
        rightMiddleLine = Line(rightTop, rightMiddle, color=WHITE)
        rightBottomLine = Line(rightMiddle, rightBottom, color=WHITE)
        bottomLine = Line(rightBottom, leftBottom, color=WHITE)
        leftBottomLine = Line(leftBottom, leftMiddle, color=WHITE)
        self.play(Create(leftMiddleLine, run_time=1))
        self.play(Create(topLine, run_time=1))
        self.play(Create(rightMiddleLine, run_time=1))
        self.play(Create(rightBottomLine, run_time=1))
        self.play(Create(bottomLine, run_time=1))
        self.play(Create(leftBottomLine, run_time=1))

        #-- now fade out the circles
        self.play(FadeOut(middleCircle, run_time=1))
        self.play(FadeOut(leftCircle, run_time=1))
        self.play(FadeOut(rightCircle, run_time=1))

        self.wait(1)
        
