"""
    Author: Ryan Setaruddin
    Date: November 8th, 2024
    Filename: Menu.py
    Purpose: creating menu with choices includes difficulty, speed, and grid sizes/
            start game, quit, pause and resume
"""

# import lib
import pygame
from Button.button import Button
from Button.button_main import *

# Menu class
class Menu:
    """docstring for Menu"""
    def __init__(self):
        game_paused, menu_state = False, "main"
        font = pygame.font.SysFont("arialblack", 40)
        TEXT_COL = (255, 255, 255)

        # load images
        path = "Images/"
        resume_img = pygame.image.load(path + "button_resume.png").convert_alpha()
        options_img = pygame.image.load(path + "button_options.png").convert_alpha()
        quit_img = pygame.image.load(path + "button_quit.png").convert_alpha()
        back_img = pygame.image.load(path + "button_back.png").convert_alpha()

        # create button instances
        resume_button = button.Button(304, 125, resume_img, 1)
        options_button = button.Button(297, 250, options_img, 1)
        quit_button = button.Button(336, 375, quit_img, 1)
        back_button = button.Button(332, 450, back_img, 1)

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
      else:
        draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

    # draw Text method
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img. (x, y))
