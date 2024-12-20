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
import os, pygame, random, sys, time

from pygame.locals import *
from constants import *

from Models.Figure import *
from Models.Tetris import *

from Button.button import Button

# introduction function
def introduction():
    # check buttons has been drawn
    if start_button.draw(screen):
        print('START')
    if exit_button.draw(screen):
        print('EXIT')

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

    game_paused, menu_state = False, "main"
    font = pygame.font.SysFont("arial", 40)
    TEXT_COL = (255, 255, 255)

    # load images
    path = "src/Button/Images/"
    start_img = pygame.image.load(os.path.join(os.getcwd(), path, "start_btn.png"))
    exit_img = pygame.image.load(os.path.join(os.getcwd(), path, "exit_btn.png"))
    resume_img = pygame.image.load(os.path.join(os.getcwd(), path, "button_resume.png"))
    options_img = pygame.image.load(os.path.join(os.getcwd(), path, "button_options.png"))
    quit_img = pygame.image.load(os.path.join(os.getcwd(), path, "button_quit.png"))
    back_img = pygame.image.load(os.path.join(os.getcwd(), path, "button_back.png"))
    # create button instances
    start_button = Button(200, 200, start_img, 0.8)
    exit_button = Button(200, 200, exit_img, 0.8)
    resume_button = Button(304, 125, resume_img, 1)
    options_button = Button(297, 250, options_img, 1)
    quit_button = Button(336, 375, quit_img, 1)
    back_button = Button(332, 450, back_img, 1)

    # screen window
    screen = pygame.display.set_mode((size))

    # title & caption
    pygame.display.set_caption('Tetris')

    # font variables
    font = pygame.font.SysFont('arial', 40)
            
    # instance
    game = Tetris(grid_width, grid_height, square_size)

    # game loop
    running = True

    while running:
  
        screen.fill((52, 78, 91))

        # call draw
        game.draw(screen)

        # call deactive 
        game.deactivate()

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
                    game_paused = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    game.downMove()

        # check if game is paused
        if game_paused == True:
            # check menu state
            if menu_state == "main":
              # draw pause screen buttons
              if resume_button.draw(screen):
                game_paused = False
              if options_button.draw(screen):
                menu_state = "options"
              if quit_button.draw(screen):
                run = False

            # check if the options menu is open
            if menu_state == "options":
              if back_button.draw(screen):
                menu_state = "main"

        # pygame update
        pygame.display.update()

        time.sleep(.5)

    # quit
    pygame.quit()
    sys.exit(0)

# run the main program
if __name__ == '__main__':
    main()