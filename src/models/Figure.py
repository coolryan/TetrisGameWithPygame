"""
    Author: Ryan Setaruddin
    Date: Oct.23, 2024
    Filename: Figure.py
    Purpose: to construct a figure class
"""

# import libraries
import pygame, random, time, sys

from pygame.locals import *
from src.constants import *

# class Figure
class Figure:
    """docstring for Figure"""
    def __init__(self, id: int, x, y, size, figureType: str, isActive: bool = False):
        self.coordList = list()
        self.id = id
        self.x, self.y = x, y
        self.type = figureType
        self.color = SHAPE_COLORS[self.type]
        self.rotationIndex = 0
        self.size = size
        # self.state = "start"
        # use to indicate which block a user can move
        self.isActive = isActive
        self.canFall = CANFALL.UNDEFINED

        self.initFigure()

    def clone(self):
        cloned_fig = Figure(self.id, self.x, self.y, self.size, self.type, self.isActive)
        cloned_fig.canFall = self.canFall
        cloned_fig.rotationIndex = self.rotationIndex
        cloned_fig.color = self.color
        cloned_fig.coordList = self.coordList
        return cloned_fig


    # initFigure method
    def initFigure(self):
        currentCoordMap = SHAPE_OFFSETS[self.type][self.rotationIndex]
        self.coordList = [(self.x + coordOffset[0], self.y + coordOffset[1]) for coordOffset in currentCoordMap]

    def __repr__(self):
        #return f"Figure: {self.type}, Id: {self.id}, x: {self.x}, y: {self.y}, state: {self.state}, active: {self.isActive}, coordList: {self.coordList}"
        return f"Figure: {self.type}, Id: {self.id}, x: {self.x}, y: {self.y}, active: {self.isActive}, coordList: {self.coordList}"
    
    def toJson(self):
        return {
            "Figure": self.type,
            "Id": self.id,
            "x": self.x,
            "y": self.y,
            "active": self.isActive,
            "coordList": self.coordList,
        }

    @classmethod
    def getRandomFigure(cls, id: int, maxX, maxY, size):
        if not hasattr(cls, "rand"):
            cls.rand = random.Random()

        x, y = cls.rand.randint(0, maxX), cls.rand.randint(0, maxY)
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

        newFig = Figure(id, x, y, size, figureType, False)
        return newFig

    # draw method
    def draw(self, screen):
        for coord in self.coordList:
            x, y = coord[0]*self.size, coord[1]*self.size
            width, height = self.size, self.size

            rect = pygame.Rect(x, y, width, height)
            pygame.draw.rect(screen, self.color, rect)

    # set methods
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

    def set_coords(self, x, y):
        self.setX(x)
        self.setY(y)


    def rotate(self, ct:int = 1):        
        self.rotationIndex = self.rotationIndex + 1
        if self.rotationIndex > 3:
            self.rotationIndex = 0

        ct -= 1
        if ct==0:
            self.initFigure()
        else:
            self.rotate(ct)

    # Todo: Do we need this? Deprecate it
    def unrotate(self):
        self.rotationIndex = self.rotationIndex - 1
        if self.rotationIndex < 0:
            self.rotationIndex = 3

        self.initFigure()

    # get methods
    def getLeft(self):
        listOfNumbers = []
        for coord in self.coordList:
            temp = coord[0]
            listOfNumbers.append(temp)

        minimum = min(listOfNumbers)
        return minimum

    def getRight(self):
        listOfNumbers = []
        for coord in self.coordList:
            temp = coord[0]
            listOfNumbers.append(temp)

        maximum = max(listOfNumbers)
        return maximum

    def getTop(self):
        listOfNumbers = []
        for coord in self.coordList:
            temp = coord[1]
            listOfNumbers.append(temp)

        minimum = min(listOfNumbers)
        return minimum

    def getBottom(self):
        listOfNumbers = []
        for coord in self.coordList:
            temp = coord[1]
            listOfNumbers.append(temp)

        maximum = max(listOfNumbers)
        return maximum
        
    def remove(self, x, y):
        coordListTemp = []

        for coord in self.coordList:
            if coord[0] == x and coord[1] == y:
                continue
            else:
                coordListTemp.append(coord)

        self.coordList = coordListTemp
