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

# create button instances
start_button = button.Button(200, 200, start_img, 0.8)
exit_button = button.Button(200, 200, exit_img, 0.8)

# check buttons has been drawn
if start_button.draw(screen):
    print('START')
if exit_button.draw(screen):
    print('EXIT')