"""
    Author: Ryan Setaruddin
    Date: November 8th, 2024
    Filename: Explosion.py
    Purpose: to develop an explosion bombs in this game 
            so that whenver the blocks touchs the ground it will exploded
"""

# import libs
import pygame
from pygame.locals import *

# Explosion class
class Explosion(pygame.sprite.Sprite):
    """docstring for Explosion"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        path = "Animations/"
        for num in range(1, 6):
            img = pygame.image.load(f"path" + "exp{num}.png").convert_alpha()
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)

        self.index, self.counter = 0, 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    # update method
    def update(self):
        explosion_speed = 4
        # update explosion animation
        self.counter += 1
        # check if counter is greater than explosion speed and check if index is less than length of images minus 1
        length = len(self.images) - 1
        if self.counter >= explosion_speed and self.index < length:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        # check if animation is complete, then reset the animation index
        if self.index >= length and self.counter >= explosion_speed:
            self.kill()

# create explosion group
explosion_group = pygame.sprite.Group()

# find the positions of explosion
pos = pygame.mouse.get_pos()

# set explosion constructor to variable then add it to explosion group
explosion = Explosion(pos[0], pos[1])
explosion_group.add(explosion)