"""
	Author: Ryan Setaruddin
	Date: May 29th, 2024
	Filename: main.py
	Purpose: To a game called tetris
"""

# import libraries
import pygame
import random
import sys
import time

from pygame.locals import *

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
	font = pygame.font.SysFont('New Times Roman', 16)
	font1 = pygame.font.SysFont('New Times Roman', 16)

	# define colors
	BLACK, WHITE, GRAY = (0, 0, 0), (255, 255, 255), (128, 128, 128)

	COLORS = [
		(0, 0, 0),
		(120, 37, 179),
		(100, 179, 179),
		(80, 34, 22),
		(80, 134, 22),
		(180, 34, 22),
		(180, 34, 122),
	]

	# game variables
	clock = pygame.time.Clock()
	fps = 60
	counter = 0
	pressing_down = False

	# class Figure
	class Figure:
		x, y = 0, 0

		figures = [
			[[2, 7, 4, 19], [8, 3, 9, 1]],
			[[8, 3, 0, 11], [6, 1, 5, 2]],
			[[0, 4, 7, 15], [, 4, 7, 2, 21]],
			[[], [], [], []],
			[[], [], [], []],
			[[], [], [], []],
			[[8, 3, 1, 10]],
		]

		"""docstring for Figure"""
		def __init__(self, x, y):
			self.x, self.y = x, y
			self.type = random.randint(0, len(self.figures) - 1)
			self.color = random.randint(1, len(COLORS) - 1)
			self.rotation = 0

		# image method
		def image(self):
			return self.figures[self.type][self.rotation]

		# rotate method
		def rotate(self):
			self.rotation = (self.rotation + 1) % len(self.figures[self.type])
			
	# class Tetris
	class Tetris:
		"""constructor"""
		def __init__(self, height, width):
			self.level, self.score = 2, 0
			self.state, self.field = "start", []
			self.height, self.width = 0, 0
			self.x, self.y = 100, 60
			self.zoom, self.figure = 20, None

			self.height, self.width = height, weight
			self.field, self.score, self.state = [], 0, "start"

			for h in range(height):
				new_line = []
				for w in range(width):
					new_line.append(0)
				self.field.append(new_line)

		# new figure methos
		def new_figure(self):
			self.figure = Figure(5, 0)

		# intersects method
		def intersects(self):
			intersection = false
			return intersection

		# break lines method
		def break_lines(self):
			pass

		# go space method
		def go_space(self):
			pass

		# go down method
		def go_down(self):
			pass

		# freeze method
		def freeze(self):
			pass

		# go side method
		def go_side(self, dx):
			pass

		def rotate(self):
			pass
			
	# instance
	game = Tetris(100, 100)

	# game loop
	running = True

	while running:
		clock.tick(fps)

		screen.fill(WHITE)
		
		# event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == K_UP:
					game.rotate()
				if event.key == K_DOWN:
					pressing_down = True
				if event.key == K_LEFT:
					game.go_side(-1)
				if event.key == K_RIGHT:
					game.go_side(1)
				if event.key == K_SPACE:
					game.go_space()
				if event.key == K_ESCAPE:
					game.__init__(20, 20)

			if event.key == pygame.KEYUP:
				if event.key == pygame.K_DOWN:
					pressing_down = False

		# looping through pygame rectange
		for gh in range(game.height):
			for gw in range(game.width):
				pygame.draw.rect(screen, GREY, [game.x + game.zoom * gw, game.y + game.zoom * gh, game.zoom, game.zoom], 1)
				if game.field[gh][gw] > 0:
					pygame.draw.rect(screen, COLORS[game.field[gh][gw]], [game.x + game.zoom * gw, game.y + game.zooom * gh + 1, game.zoom - 2, game.zoom - 1])

		# pygame update
		pygame.display.update()

	# quit
	pygame.quit()
	sys.exit(0)

# run the main program
if __name__ == '__main__':
	main()