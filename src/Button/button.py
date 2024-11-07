"""
    Author: Ryan Setaruddin
    Date: November 6th, 2024
    Filename: button.py
    Purpose: construct a button class and blueprint on how to create button
"""

# Button class
class Button:
    """docstring for Button"""
    def __init__(self, x, y, image, scale):
        width, height = image.get_width(), image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    # draw method
    def draw(self, surface):
        # create a variable called action & set to False
        action = False

        # get the mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clciked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self..rect.x, self.rect.y))

        return False
