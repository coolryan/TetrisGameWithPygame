"""
    Author: Ryan Setaruddin
    Date: May 29th, 2024
    Filename: main.py
    Purpose: to execuate the main program
"""

"""
    To do: Translate from coordinate system to grid index system. For drawing, will dynamically convert to x,y coordinates again.
	To do: Translate from coordinate system to grid index system. 
	For drawing, will dynamically convert to x, y coordinates again.
"""

# import libraries
import pygame, random, time, sys

from pygame.locals import *
from constants import *

from Figure import *
from Tetris import *

# introduction function
def introduction():
    pass

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# define main function
def main():
    # initialize pygame
    pygame.init()

    # Size in grid
    grid_width, grid_height, square_size = 10, 20, 50
    size = (grid_width*square_size, grid_height*square_size)

    # screen window
    screen = pygame.display.set_mode((size))

    # title & caption
    pygame.display.set_caption('Tetris')

    # font variables
    font = pygame.font.SysFont('ariablack', 40)
            
    # instance
    game = Tetris(grid_width, grid_height, square_size)

    # game loop
    running = True

    while running:
  
        screen.fill(BLACK)

        # call draw
        game.draw(screen)

        # call deactive 
        game.deactivate()

        # call move
        # game.move()

        # call new figures
        if game.getActiveFigure() is None:
            game.newFigure()
        
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

        # pygame update
        pygame.display.update()

        time.sleep(.5)

    # quit
    pygame.quit()
    sys.exit(0)

# run the main program
if __name__ == '__main__':
    main()