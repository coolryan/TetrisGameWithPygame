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
from Figure import *

# class Tetris
class Tetris:
	"""constructor"""
	def __init__(self, height, width):
		self.level, self.score = 2, 0
		self.state = "start"
		self.height, self.width = height, width
		self.speed = 10
		self.figures, self.nextFigures = [], []
		self.initFigures()

	def initFigures(self):
		self.nextFigures.append(Figure.getRandomFigure(self.width, self.height, FIGURE_WIDTH, FIGURE_HEIGHT))
		self.nextFigures.append(Figure.getRandomFigure(self.width, self.height, FIGURE_WIDTH, FIGURE_HEIGHT))
		self.nextFigures.append(Figure.getRandomFigure(self.width, self.height, FIGURE_WIDTH, FIGURE_HEIGHT))
		self.nextFigures.append(Figure.getRandomFigure(self.width, self.height, FIGURE_WIDTH, FIGURE_HEIGHT))

	# new figure method
	def newFigure(self):
		nextFig = self.nextFigures.pop()

		nextFig.setX(500)
		nextFig.setY(0)
		nextFig.isActive = True

		self.nextFigures.append(Figure.getRandomFigure(self.width, self.height, FIGURE_WIDTH, FIGURE_HEIGHT))

		self.figures.append(nextFig)

		print(f"\nnew figure's x:{nextFig.x}, y:{nextFig.y}")

	def getActiveFigure(self):
		for fig in self.figures:
			if fig.isActive:
				return fig

	# draw method
	def draw(self, screen):
		for fig in self.figures:
			fig.draw(screen)

	def deactivate(self):
		for fg in self.figures:
			if fg.state == "stop" and fg.isActive:
				fg.isActive = False

	# move method
	def move(self):
		for fig in self.figures:
			if fig.state == "start":
				moveAmount = self.speed if (self.height - fig.getBottom()) >= self.speed else (self.height - fig.getBottom())
				fig.setY(fig.y-moveAmount)

			if fig.getBottom() >= self.height:
				fig.state = "stop"

	# leftMove method
	def leftMove(self):
		for fig in self.figures:
			if fig.isActive and fig.getLeft() >= 0:
				moveAmount = fig.width if fig.getLeft() >= fig.width else fig.getLeft()
				fig.setX(fig.x-moveAmount)

	# x:160 FigWidth: 60 ScreenWidth: 1000 Move: 840
	# rightMove method
	def rightMove(self):
		for fig in self.figures:
			if fig.isActive and fig.getRight() <= self.width:
				moveAmount = fig.width if (self.width - fig.getRight()) >= fig.width else (self.width - fig.getRight())
				fig.setX(fig.x+moveAmount)

	# downMove method
	def downMove(self):
		for fig in self.figures:
			if fig.isActive and fig.getBottom() <= self.height:
				moveAmount = fig.height if (self.height - fig.getBottom()) >= fig.height else (self.height - fig.getBottom())
				fig.setY(fig.y-moveAmount)

			if fig.getBottom() >= self.height:
				fig.state = "stop"

	# rotate method
	def rotate(self):
		pass