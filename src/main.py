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
		print("draw")
		for coord in self.coordList:
			rect = pygame.Rect(coord[0], coord[1], self.width, self.height)
			pygame.draw.rect(screen, self.color, rect)

	# get bottom method
	def getBottom(self):
		listOfNumbers = []
		for h in self.coordList:
			temp = h[1]
			listOfNumbers.append(temp)

		maximum = max(listOfNumbers)

		totalMax = maximum + self.height
		return totalMax
		
# class Tetris
class Tetris:
	"""constructor"""
	def __init__(self, height, width):
		self.level, self.score = 2, 0
		self.state, self.field = "start", []
		self.height, self.width = height, width
		self.zoom, self.figure = 20, None

		for h in range(height):
			new_line = []
			for w in range(width):
				new_line.append(0)
			self.field.append(new_line)

	# new figure method
	def new_figure(self):
		self.figures = [
			Figure(100, 100, 60, 60, I_TETROMINO),
			Figure(200, 200, 60, 60, O_TETROMINO),
			Figure(300, 300, 60, 60, T_TETROMINO),
			Figure(100, 400, 60, 60, L_TETROMINO),
			Figure(300, 500, 60, 60, J_TETROMINO),
			Figure(500, 500, 60, 60, S_TETROMINO),
			Figure(650, 650, 60, 60, Z_TETROMINO)
		]

	# draw method
	def draw(self, screen):
		for trs in self.figures:
			trs.draw(screen)

	# move method
	def move(self):
		for trs in self.figures:
			if trs.state == "start":
				coordListTemp = []
				
				for coord in trs.coordList:
					coordListTemp.append((coord[0], coord[1]+10))

				trs.coordList = coordListTemp
			else:
				print("Figure stop")
		
			if trs.getBottom() >= self.height:
				trs.state = "stop"

	# leftMove method
	def leftMove(self):
		for fig in self.figures:
			if fig == self.isActive:
				coordListTemp = []
				for coord in fig.coordList:
					coordListTemp.append((coord[0]-fig.width, coord[1]))
				fig.coordList = coordListTemp

	# rightMove method
	def rightMove(self):
		for fig in self.figures:
			if fig == self.isActive:
				coordListTemp = []
				for coord in fig.coordList:
					coordListTemp.append((coord[0]+fig.width, coord[1]))
				fig.coordList = coordListTemp

	# downMove method
	def downMove(self):
		for fig in self.figures:
			if fig == self.isActive:
				coordListTemp = []
				for coord in fig.coordList:
					coordListTemp.append((coord[0], coord[1]-fig.height))
				fig.coordList = coordListTemp

	# rotate method
	def rotate(self):
		pass

# define main function
def main():
	# initialize pygame
	pygame.init()

	# define size by width & height
	size = (800, 800)

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

	# call new figures
	game.new_figure()

	# game loop
	running = True

	while running:
		time.sleep(1)

		screen.fill(BLACK)

		# call draw
		game.draw(screen)

		# call move
		game.move()

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
					game.rotate()
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

	# quit
	pygame.quit()
	sys.exit(0)

# run the main program
if __name__ == '__main__':
	main()