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
	font = pygame.font.SysFont('timesroman', 16, True, False)
	font2 = pygame.font.SysFont('timesroman', 20, True, False)

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
			"I_TETROMINO"
		    "O_TETROMINO"
		    "T_TETROMINO"
		    "L_TETROMINO"
		    "J_TETROMINO"
		    "S_TETROMINO"
		    "Z_TETROMINO"
		]

		"""docstring for Figure"""
		def __init__(self, x, y):
			self.x, self.y = x, y
			self.type = random.randint(0, len(self.figures) - 1)
			self.color = random.randint(1, len(COLORS) - 1)
			self.rotation = 0

		# draw method
		def draw(self):
			for i in range(x):
				for j in range(y):
					rect = pygame.Rect(50, 50, i, j)

			pygame.draw.rect(screen, BLACK, rect, 2)

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

			self.height, self.width = height, width
			self.field, self.score, self.state = [], 0, "start"

			for h in range(height):
				new_line = []
				for w in range(width):
					new_line.append(0)
				self.field.append(new_line)

		# new figure method
		def new_figure(self):
			self.figure = Figure(10, 10)

		# intersects method
		def intersects(self):
			intersection = False
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

		screen.fill(BLACK)

		# if game.figure is None:
		# 	game.new_figure()

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

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_DOWN:
					pressing_down = False

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