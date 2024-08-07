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
class Figure(pbject):
	"""docstring for Figure"""
	def __init__(self, x, y, width, height, figureType: str):
		self.coordList = list()

		self.x, self.y = x, y
		# self.type = random.randint(0, len(self.figures) - 1)
		self.type = figureType
		self.color = random.randint(1, len(COLORS) - 1)
		self.rotation = 0
		self.width, self.height = width, height
		self.state = "start"

		self.initFigure()

	# initFigure method
	def initFigure(self):
		self.coordList

	# draw method
	def draw(self):
		if self.type == I_TETROMINO:
			for r in range(4):
				rect = pygame.Rect(self.x, (self.y+r*self.height), self.width, self.height)
				pygame.draw.rect(screen, COLORS[1], rect)

		elif self.type == O_TETROMINO:
			rect1 = pygame.Rect(self.x, self.y, self.width, self.height)
			rect2 = pygame.Rect((self.x+self.width), self.y, self.width, self.height)
			rect3 = pygame.Rect(self.x, (self.y-self.height), self.width, self.height)
			rect4 = pygame.Rect((self.x+self.width), (self.y-self.height), self.width, self.height)

			for rect in [rect1, rect2, rect3, rect4]:
				pygame.draw.rect(screen, COLORS[2], rect)

		elif self.type == T_TETROMINO:
			rect1 = pygame.Rect(self.x, self.y, self.width, self.height)
			rect2 = pygame.Rect((self.x+self.width), self.y, self.width, self.height)
			rect3 = pygame.Rect((self.x+self.width*2), self.y, self.width, self.height)
			rect4 = pygame.Rect((self.x+self.width), (self.y+self.height), self.width, self.height)

			for rect in [rect1, rect2, rect3, rect4]:
				pygame.draw.rect(screen, COLORS[3], rect)

		elif self.type == L_TETROMINO:
			rect1 = pygame.Rect(self.x, self.y, self.width, self.height)
			rect2 = pygame.Rect(self.x, (self.y+self.height), self.width, self.height)
			rect3 = pygame.Rect(self.x, (self.y+self.height*2), self.width, self.height)
			rect4 = pygame.Rect((self.x+self.width), (self.y+self.height*2), self.width, self.height)

			for rect in [rect1, rect2, rect3, rect4]:
				pygame.draw.rect(screen, COLORS[4], rect)

		elif self.type == J_TETROMINO:
			rect1 = pygame.Rect(self.x, self.y, self.width, self.height)
			rect2 = pygame.Rect(self.x, (self.y+self.height), self.width, self.height)
			rect3 = pygame.Rect(self.x, (self.y+self.height*2), self.width, self.height)
			rect4 = pygame.Rect((self.x-self.width), (self.y+self.height*2), self.width, self.height)

			for rect in [rect1, rect2, rect3, rect4]:
				pygame.draw.rect(screen, COLORS[5], rect)

		elif self.type == S_TETROMINO:
			rect1 = pygame.Rect(self.x, self.y, self.width, self.height)
			rect2 = pygame.Rect(self.x+self.width, self.y, self.width, self.height)
			rect3 = pygame.Rect(self.x, (self.y+self.height), self.width, self.height)
			rect4 = pygame.Rect((self.x-self.width), (self.y+self.height), self.width, self.height)

			for rect in [rect1, rect2, rect3, rect4]:
				pygame.draw.rect(screen, COLORS[6], rect)

		elif self.type == Z_TETROMINO:
			rect1 = pygame.Rect(self.x, self.y, self.width, self.height)
			rect2 = pygame.Rect((self.x-self.width), self.y, self.width, self.height)
			rect3 = pygame.Rect(self.x, (self.y+self.height), self.width, self.height)
			rect4 = pygame.Rect((self.x+self.width), (self.y+self.height), self.width, self.height)

			for rect in [rect1, rect2, rect3, rect4]:
				pygame.draw.rect(screen, COLORS[0], rect)

	# rotate method
	def rotate(self):
		pass

	# get bottom method
	def getBottom(self):
		pass
		
# class Tetris
class Tetris(Figure):
	"""constructor"""
	def __init__(self, height, width):
		self.level, self.score = 2, 0
		self.state, self.field = "start", []
		self.height, self.width = height, width
		self.x, self.y = 100, 60
		self.zoom, self.figure = 20, None
		self.field, self.score, self.state = [], 0, "start"

		for h in range(height):
			new_line = []
			for w in range(width):
				new_line.append(0)
			self.field.append(new_line)

	# new figure method
	def new_figure(self):
		TETROMINOS = [
			Figure(100, 100, 60, 60, I_TETROMINO),
			# Figure(200, 200, 60, 60, O_TETROMINO),
			# Figure(300, 300, 60, 60, T_TETROMINO),
			# Figure(100, 400, 60, 60, L_TETROMINO),
			# Figure(300, 500, 60, 60, J_TETROMINO),
			# Figure(500, 500, 60, 60, S_TETROMINO),
			# Figure(650, 650, 60, 60, Z_TETROMINO)
		]

	# draw method
	def draw(self):
		for trs in TETROMINOS:
			trs.draw()

	# move method
	def move(self):
		for trs in TETROMINOS:
			if trs.state == "start":
				trs.y += 1

			print(trs.y, self.height, trs.state)
		
			if trs.y >= self.height:
				trs.state = "stop"

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

	# constants colors
	constants.BLACK
	constants.COLORS

	# game variables
	clock = pygame.time.Clock()
	fps = 60
	counter = 0
	pressing_down = False 
			
	# instance
	game = Tetris(size[0], size[1])

	# call new figures
	game.new_figure()

	# game loop
	running = True

	while running:
		clock.tick(fps)

		screen.fill(BLACK)

		# call draw
		game.draw()

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
				if event.key == K_UP:
					pass
				if event.key == K_DOWN:
					pass
				if event.key == K_LEFT:
					pass
				if event.key == K_RIGHT:
					pass
				if event.key == K_SPACE:
					pass
				if event.key == K_ESCAPE:
					game.__init__(20, 20)

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_DOWN:
					pass

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