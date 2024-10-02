"""
	Author: Ryan Setaruddin
	Date: May 29th, 2024
	Filename: main.py
	Purpose: to execuate the main program
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
		# self.type = random.randint(0, len(self.figures) - 1)
		self.type = figureType
		#self.color = random.randint(1, len(COLORS) - 1)
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

	# draw method
	def draw(self, screen):
		for coord in self.coordList:
			rect = pygame.Rect(coord[0], coord[1], self.width, self.height)
			pygame.draw.rect(screen, self.color, rect)

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
		
# class Tetris
class Tetris:
	"""constructor"""
	def __init__(self, height, width):
		self.level, self.score = 2, 0
		self.state = "start"
		self.height, self.width = height, width
		self.speed = 10
		self.figures = []
		self.nextFigures = []

	# new figure method
	def newFigure(self):
		self.figures.append(Figure(500, 0, 60, 60, I_TETROMINO, True))

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
				coordListTemp = []
				
				for coord in fig.coordList:
					coordListTemp.append((coord[0], coord[1]+self.speed))

				fig.coordList = coordListTemp

			if fig.getBottom() >= self.height:
				fig.state = "stop"

	# leftMove method
	def leftMove(self):
		for fig in self.figures:
			if fig.isActive and fig.getLeft() >= 0:
				coordListTemp = []
				moveAmount = fig.width if fig.getLeft() >= fig.width else fig.getLeft()
				print(f'x:{fig.getLeft()} width: {fig.width} amount of move: {moveAmount}')
				for coord in fig.coordList:
					coordListTemp.append((coord[0]-moveAmount, coord[1]))
				fig.coordList = coordListTemp

	# x:160 FigWidth: 60 ScreenWidth: 1000 Move: 840
	# rightMove method
	def rightMove(self):
		for fig in self.figures:
			if fig.isActive and fig.getRight() <= self.width:
				coordListTemp = []
				moveAmount = fig.width if (self.width - fig.getRight()) >= fig.width else (self.width - fig.getRight())
				print(f'x:{fig.getRight()} FigWidth: {fig.width} ScreenWidth: {self.width} Move: {moveAmount}')
				for coord in fig.coordList:
					coordListTemp.append((coord[0]+moveAmount, coord[1]))
				fig.coordList = coordListTemp

	# downMove method
	def downMove(self):
		for fig in self.figures:
			if fig.isActive and fig.getBottom() <= self.height:
				coordListTemp = []
				moveAmount = fig.height if (self.height - fig.getBottom()) >= fig.height else (self.height - fig.getBottom())
				print(f'y:{fig.getBottom()} Height: {fig.height} amount of move: {moveAmount}')
				for coord in fig.coordList:
					coordListTemp.append((coord[0], coord[1]+moveAmount))
				fig.coordList = coordListTemp

	# rotate method
	def rotate(self):
		pass

# define main function
def main():
	# initialize pygame
	pygame.init()

	# define size by width & height
	size = (1000, 1000)

	# screen window
	screen = pygame.display.set_mode((size))

	# title & caption
	pygame.display.set_caption('Tetris')

	# font variables
	font = pygame.font.SysFont('timesroman', 16, True, False)
	font2 = pygame.font.SysFont('timesroman', 20, True, False)

	# game variables
	counter = 0
	pressing_down = False 
			
	# instance
	game = Tetris(size[0], size[1])

	# game loop
	running = True

	while running:

		screen.fill(BLACK)

		# call draw
		game.draw(screen)

		# call deactive 
		game.deactivate()

		# call move
		game.move()

		# call new figures
		if game.getActiveFigure() is None:
			game.newFigure()

		# counter += 1

		# if counter > 100000:
		# 	counter = 0

		# if counter % (fps // game.level // 2) == 0 or pressing_down:
		# 	if game.state == "start":
		# 		game.go_down()
		
		# event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == K_DOWN:
					game.downMove()
				if event.key == K_LEFT:
					game.leftMove()
				if event.key == K_RIGHT:
					game.rightMove()
				if event.key == K_SPACE:
					#game.rotate()
					pass
				if event.key == K_ESCAPE:
					game.__init__(20, 20)

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_DOWN:
					game.downMove()

		# text = font.render("Score: " + str(game.score), True, Black)
		# text_game_over = font2.render("Game Over", True, Grey)
		# press_esc = font2.render("press ESC", True, Grey)

		# screen.blit(text, (0, 0))

		# if game.state == "gameover":
		# 	screen.blit(text_game_over, (0, 0))
		# 	screen.blit(press_esc, (0, 0))

		# pygame update
		pygame.display.update()

		time.sleep(.5)

	# quit
	pygame.quit()
	sys.exit(0)

# run the main program
if __name__ == '__main__':
	main()