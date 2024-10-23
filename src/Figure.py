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
	def __init__(self, x, y, width, height, figureType: str, isActive: bool = False):
		self.coordList = list()
		self.x, self.y = x, y
		self.type = figureType
		self.color = COLORS[0]
		self.rotation = 0
		self.width, self.height = width, height
		self.state = "start"
		self.isActive = isActive

		self.initFigure()

	# initFigure method
	def initFigure(self):
		#  [ ] [(x,y), [x,y+4], [0,8], [0.12]]
		if self.type == I_TETROMINO:
			self.coordList = [(self.x, self.y+i*self.height) for i in range(4)]

		elif self.type == O_TETROMINO:
			self.coordList = [
				(self.x, self.y),
				(self.x+self.width, self.y),
				(self.x, self.y-self.height),
				(self.x+self.width, self.y-self.height)
			]
		elif self.type == T_TETROMINO:
			self.coordList = [
				(self.x, self.y),
				(self.x+self.width, self.y),
				(self.x+self.width*2, self.y),
				(self.x+self.width, self.y+self.height)
			]
		elif self.type == L_TETROMINO:
			self.coordList = [
				(self.x, self.y),
				(self.x, self.y+self.height),
				(self.x, self.y+self.height*2),
				(self.x+self.width, self.y+self.height*2)
			]
		elif self.type == J_TETROMINO:
			self.coordList = [
				(self.x, self.y),
				(self.x, self.y+self.height),
				(self.x, self.y+self.height*2),
				(self.x-self.width, self.y+self.height*2)
			]
		elif self.type == S_TETROMINO:
			self.coordList = [
				(self.x, self.y),
				(self.x+self.width, self.y),
				(self.x, self.y+self.height),
				(self.x-self.width, self.y+self.height)
			]
		elif self.type == Z_TETROMINO:
			self.coordList = [
				(self.x, self.y),
				(self.x-self.width, self.y),
				(self.x, self.y+self.height),
				(self.x+self.width, self.y+self.height)
			]

	@classmethod
	def getRandomFigure(cls, maxX, maxY, width, height):
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

		newFig = Figure(x, y, width, height, figureType, False)
		return newFig

	# draw method
	def draw(self, screen):
		for coord in self.coordList:
			rect = pygame.Rect(coord[0], coord[1], self.width, self.height)
			pygame.draw.rect(screen, self.color, rect)

	def setX(self, x):
		diff = self.x - x
		self.x = x
		coordListTemp = []
		
		for coord in self.coordList:
			coordListTemp.append((coord[0]-diff, coord[1]))
		
		self.coordList = coordListTemp


	def setY(self, y):
		diff = self.y - y
		self.y = y
		coordListTemp = []

		for coord in self.coordList:
			coordListTemp.append((coord[0], coord[1]-diff))

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

		totalMax = maximum + self.width
		return totalMax

	# get bottom method
	def getBottom(self):
		listOfNumbers = []
		for coord in self.coordList:
			temp = coord[1]
			listOfNumbers.append(temp)

		maximum = max(listOfNumbers)

		totalMax = maximum + self.height
		return totalMax