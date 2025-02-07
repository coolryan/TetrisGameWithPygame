"""
    Author: Ryan Setaruddin
    Date: Oct. 23, 2024
    Filename: Tetris.py
    Purpose: to construct a Tetris class
"""

# import libraries
import pygame, random, time, sys

from pygame.locals import *
from constants import *
from .Figure import *

# class TetrisGame
class TetrisGame:
    # Class state
    currentFigureIndex = 0

    """constructor"""
    def __init__(self, width, height, square_size):
        self.level, self.score = 2, 0
        self.state = GAMESTATE.RUNNING
        self.height, self.width = height, width
        self.velocity = 1
        self.figures, self.nextFigures = [], []
        self.square_size = square_size
        self.initFigures()
        # Grid is by y then x. So grid[y][x]
        self.grid = [[None for i in range(width)] for j in range(height)]

    @classmethod
    def _getNextFigureId(cls) -> int:
        cls.currentFigureIndex += 1
        return cls.currentFigureIndex


    def initFigures(self):
        self.nextFigures.append(Figure.getRandomFigure(self._getNextFigureId(), self.width, self.height, self.square_size))
        self.nextFigures.append(Figure.getRandomFigure(self._getNextFigureId(), self.width, self.height, self.square_size))
        self.nextFigures.append(Figure.getRandomFigure(self._getNextFigureId(), self.width, self.height, self.square_size))
        self.nextFigures.append(Figure.getRandomFigure(self._getNextFigureId(), self.width, self.height, self.square_size))

    # new figure method
    def newFigure(self):
        nextFig: Figure = self.nextFigures.pop()

        nextFig.setX(self.width//2)
        nextFig.setY(-4)
        nextFig.isActive = True

        self.nextFigures.append(Figure.getRandomFigure(self._getNextFigureId(), self.width, self.height, self.square_size))

        self.figures.append(nextFig)

    def getActiveFigure(self):
        for fig in self.figures:
            if fig.isActive:
                return fig
            
    def updateGrid(self):
        # Reset the grid
        self.grid = [[None for i in range(self.width)] for j in range(self.height)]
        # Add each figure's coords to the grid
        for fig in self.figures:
            for coord in fig.coordList:
                try:
                    x, y = coord[0], coord[1]
                    self.grid[y][x] = fig
                except IndexError as e:
                    continue    

    # draw method
    def draw(self, screen):
        for fig in self.figures:
            fig.draw(screen)

    def deactivate(self):
        for fg in self.figures:
            if fg.state == "stop" and fg.isActive:
                fg.isActive = False

    def checkGameState(self):
        for fig in self.figures:
            if fig.state == "stop" and fig.getTop() < 0:
                self.state = GAMESTATE.GAMEOVER

    # clear method
    def clearFullRows(self):
        rowCleared = False

        for y, row in enumerate(reversed(self.grid)):
            isRowFull = True
            for x, gridLocation in enumerate(row):
                if gridLocation is None:
                    isRowFull = False
                elif rowCleared and gridLocation is not None:
                    gridLocation.state = "start"

            if isRowFull:
                for x, fig in enumerate(row):
                    fig.remove(x, y)
                rowCleared = True

        self.updateGrid()

    # distance funnction helpers
    def distanceDownActive(self):
        activeFigure = self.getActiveFigure()
        if activeFigure is None:
            return 0

        # find minimum space open from all block in active figure
        emptySpacePerCoord = []
        for coord in activeFigure.coordList:
            # Check how many empty spaces underneath
            spacesUnder, emptySpace, empty = 0, 0, True
            y, x = coord[1], coord[0]

            while empty:
                spacesUnder += 1
                if y+spacesUnder >= self.height:
                    break

                if self.grid[y+spacesUnder][x] is None or self.grid[y+spacesUnder][x] is activeFigure:
                    emptySpace = spacesUnder
                else:
                    empty = False

            emptySpacePerCoord.append(emptySpace)
        return min(emptySpacePerCoord)            
                
    def distanceLeftActive(self):
        activeFigure = self.getActiveFigure()
        if activeFigure is None:
            return 0

    def distanceRightActive(self):
        activeFigure = self.getActiveFigure()
        if activeFigure is None:
            return 0

    # move method
    def move(self):
        for fig in self.figures:
            if fig.state == "start":
                spaceLeft = self.height - fig.getBottom() - 1
                enoughSpace = self.velocity < spaceLeft
                moveAmount = self.velocity if enoughSpace else spaceLeft

                if self.willCollide(fig=fig, dx=0, dy=moveAmount):
                    fig.state = "stop"
                else:
                    fig.setY(fig.y+moveAmount)

            if fig.getBottom() == self.height -1:
                fig.state = "stop"

    # leftMove method
    def leftMove(self):
        for fig in self.figures:
            if fig.isActive and fig.getLeft() >= 0:
                moveAmount = -1 if fig.getLeft() > 0 else fig.getLeft()

                if self.willCollide(fig=fig, dx=moveAmount, dy=0):
                    continue
                else:
                    fig.setX(fig.x+moveAmount)

    # x:160 FigWidth: 60 ScreenWidth: 1000 Move: 840
    # rightMove method
    def rightMove(self):
        for fig in self.figures:
            if fig.isActive and fig.getRight() <= self.width:
                moveAmount = 1 if (self.width - fig.getRight()) > 1 else 0

                if self.willCollide(fig=fig, dx=moveAmount, dy=0):
                    continue
                else:
                    fig.setX(fig.x+moveAmount)

    # downMove method
    def downMove(self):
        for fig in self.figures:
            if fig.isActive and fig.getBottom() <= self.height:
                spaceLeft = self.height - fig.getBottom() - 1
                enoughSpace = self.velocity < spaceLeft
                moveAmount = self.velocity if enoughSpace else spaceLeft

                if self.willCollide(fig=fig, dx=0, dy=moveAmount):
                    continue
                else:
                    fig.setY(fig.y+moveAmount)

            if fig.getBottom() == self.height -1:
                fig.state = "stop"

    # rotate method
    def rotate(self):
        for fig in self.figures:
            if fig.isActive:
                fig.rotate()
                break

    def willCollide(self, fig, dx, dy):
        """
            Check the new coordinates of the figure, and see if anything other than itself is on the grid at those locations
        """
        # Calculate the new coordinates (without actually changing them in the figure)
        newCoordList = [(coord[0]+dx, coord[1]+dy) for coord in fig.coordList]
        # Make sure none of the new coordinates already have shapes in them
        for coord in newCoordList:
            x, y = coord[0], coord[1]
            if x<0 or y<0:
                continue

            shapeAtCoord = self.grid[y][x] is not None
            thisFigAtCoord = self.grid[y][x] is fig

            if shapeAtCoord and not thisFigAtCoord:
                return True
        return False