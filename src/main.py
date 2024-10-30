"""
	Author: Ryan Setaruddin
	Date: May 29th, 2024
	Filename: main.py
	Purpose: to execuate the main program
"""

"""
	To do: Translate from coordinate system to grid index system. 
	For drawing, will dynamically convert to x, y coordinates again.
"""

# import libraries
import pygame, random, time, sys

from pygame.locals import *
from constants import *

from Figure import *
from Tetris import *

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