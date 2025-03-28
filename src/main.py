"""
    Author: Ryan Setaruddin
    Date: May 29th, 2024
    Filename: main.py
    Purpose: to execuate the main program
"""

"""
    To do: Translate from coordinate system to grid index system. 
    For drawing, will dynamically convert to x,y coordinates again.
"""

# import libraries
import os, pygame, random, sys, time

from pygame.locals import *
from constants import *

from models.Figure import *
from models.TetrisGame import *

#from Button.Button import Button

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# define main function
def main():
    # initialize pygame
    pygame.init()

    game_width, game_height = 20, 25
    grid_location_x, grid_location_y = 5, 0

    # Size in grid
    grid_width, grid_height, square_size = 10, 20, 50
    tetris = TetrisGame(game_width, game_height, grid_location_x, grid_location_y,
        grid_width, grid_height, square_size)

    tetris.start()

# run the main program
if __name__ == '__main__':
    main()