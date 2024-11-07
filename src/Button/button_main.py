"""
    Author: Ryan Setaruddin
    Date: November 6th, 2024
    Filename: button_main.py
    Purpose: implemnet buttons on the screen and make sure to has clciked ability
"""
# import libs
import pygame
import button

# load button images
path = "Images/"
start_img = pygame.image.load(path + "start_btn.png").convert_alpha()
exit_img = pygame.image.load(path + "exit_btn.png").convert_alpha()

# create  button instances
start_button = button.Button()
exit_button = button.Button()