"""
    Author: Ryan Setaruddin
    Date: Oct.23, 2024
    Filename: Figure.py
    Purpose: to construct a figure class
"""

# import libraries
import pygame, random, time, sys

from pygame.locals import *
from constants import *

# class Figure
class Figure:
    """docstring for Figure"""
    def __init__(self, x, y, size, figureType: str, isActive: bool = False):
        self.coordList = list()
        self.x, self.y = x, y
        self.type = figureType
        self.color = COLORS[0]
        self.rotation = 0
        self.size = size
        self.state = "start"
        self.isActive = isActive

        self.initFigure()

    # initFigure method
    def initFigure(self):
        print(f"Init figure: {self.x}, {self.y}, {self.size}, {self.type}")

        if self.type == I_TETROMINO:
            self.coordList = [(self.x, self.y+i) for i in range(4)]

        elif self.type == O_TETROMINO:
            self.coordList = [
                (self.x, self.y),
                (self.x+1, self.y),
                (self.x, self.y+1),
                (self.x+1, self.y+1)
            ]
        elif self.type == T_TETROMINO:
            self.coordList = [
                (self.x, self.y),
                (self.x+1, self.y),
                (self.x+2, self.y),
                (self.x+1, self.y+1)
            ]
        elif self.type == L_TETROMINO:
            self.coordList = [
                (self.x, self.y),
                (self.x, self.y+1),
                (self.x, self.y+2),
                (self.x+1, self.y+2)
            ]
        elif self.type == J_TETROMINO:
            self.coordList = [
                (self.x, self.y),
                (self.x, self.y+1),
                (self.x, self.y+2),
                (self.x-1, self.y+2)
            ]
        elif self.type == S_TETROMINO:
            self.coordList = [
                (self.x, self.y),
                (self.x+1, self.y),
                (self.x, self.y+1),
                (self.x-1, self.y+1)
            ]
        elif self.type == Z_TETROMINO:
            self.coordList = [
                (self.x, self.y),
                (self.x-1, self.y),
                (self.x, self.y+1),
                (self.x+1, self.y+1)
            ]
        print("CoordList: ", self.coordList)

    @classmethod
    def getRandomFigure(cls, maxX, maxY, size):
        if not hasattr(cls, "rand"):
            cls.rand = random.Random()

        x = cls.rand.randint(0, maxX)
        y = cls.rand.randint(0, maxY)
        shapeIndex = cls.rand.randint(0, 6)

        if shapeIndex == 0:
            figureType = I_TETROMINO
        elif shapeIndex == 1:
            figureType = O_TETROMINO
        elif shapeIndex == 2:
            figureType = T_TETROMINO
        elif shapeIndex == 3:
            figureType = L_TETROMINO
        elif shapeIndex == 4:
            figureType = J_TETROMINO
        elif shapeIndex == 5:
            figureType = S_TETROMINO
        elif shapeIndex == 6:
            figureType = Z_TETROMINO

        newFig = Figure(x, y, size, figureType, False)
        return newFig

    # draw method
    def draw(self, screen):
        print("Size: ", self.size)
        print("Drawing coords: ", self.coordList)
        for coord in self.coordList:
            x = coord[0]*self.size
            y = coord[1]*self.size
            width = self.size
            height = self.size
            print(f"x: {x} y: {y}")
            rect = pygame.Rect(x, y, width, height)
            pygame.draw.rect(screen, self.color, rect)

    def setX(self, x):
        diff = self.x - x
        self.x = x
        coordListTemp = []
        
        for coord in self.coordList:
            coordListTemp.append(
                ((coord[0]-diff), coord[1])
            )
        
        self.coordList = coordListTemp


    def setY(self, y):
        diff = self.y - y
        self.y = y
        coordListTemp = []

        for coord in self.coordList:
            coordListTemp.append(
                (coord[0], (coord[1]-diff))
            )

        self.coordList = coordListTemp


    # get left method
    def getLeft(self):
        listOfNumbers = []
        for coord in self.coordList:
            temp = coord[0]
            listOfNumbers.append(temp)

        minimum = min(listOfNumbers)
        return minimum

    # get right method
    def getRight(self):
        listOfNumbers = []
        for coord in self.coordList:
            temp = coord[0]
            listOfNumbers.append(temp)

        maximum = max(listOfNumbers)

        totalMax = maximum
        return totalMax

    # get bottom method
    def getBottom(self):
        listOfNumbers = []
        for coord in self.coordList:
            temp = coord[1]
            listOfNumbers.append(temp)

        maximum = max(listOfNumbers)

        totalMax = maximum
        return totalMax
