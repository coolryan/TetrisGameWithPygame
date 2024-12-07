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
        
    # draw Text method
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img. (x, y))
