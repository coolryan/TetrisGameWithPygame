# import library
import pygame
import sys
import random

from pygame import Rect, K_LEFT, K_RIGHT, K_UP, K_DOWN

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

	# define colors
	BLACK, WHITE, GRAY = (0, 0, 0), (255, 255, 255), (128, 128, 128)

	# game varaibles
	clock = pygame.time.Clock()
	fps = 60
	counter = 0

	# class tetris
	class Tetris:
		"""constructor"""
		def __init__(self, height, weight):
			self.level, self.score = 2, 0
			self.state, self.field = "start", []
			self.height, slef.width = 0, 0
			self.x, self.y = 100, 60
			self.zoom, self.figure = 20, None

			self.height, slef.width = height, weight
			self.field, self.score, self.state = [], 0, "start"
			

	# game loop
	running = True

	while running:
		clock.tick(fps)

		screen.fill(WHITE)

		x, y = 0, 0
		
		# event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == K_UP:
					x = -5
					y = 0
				if event.key == K_DOWN:
					x = 5
					y = 0
				if event.key == K_LEFT:
					x = 0
					y = -5
				if event.key == K_RIGHT:
					x = 0
					y = 5
				if event.key == K_SPACE:
					x = 0
					y = 5
				if event.key == K_ESCAPE:
					x = 0
					y = 5

			if event.key == pygame.KEYUP:
				if event.key == pygame.K_DOWN:
					pass

			rect2.move_ip(x, y)

		# draw rectangle
		pygame.draw.rect(screen, red, rect1)
		pygame.draw.rect(screen, blue, rect2)

		# pygame update
		pygame.display.update()

	# quit
	pygame.quit()
	sys.exit(0)

# run the main program
if __name__ == '__main__':
	main()