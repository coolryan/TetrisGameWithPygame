"""
    Author: Ryan Setaruddin
    Date: Oct. 23, 2024
    Filename: Tetris.py
    Purpose: to construct a Tetris class
"""

# import libraries
import pygame, random, time, sys

from pygame.locals import *
from constants import *
from .Figure import *

# class TetrisGame
class TetrisGame:
    # Class state
    currentFigureIndex = 0

    """constructor"""
    def __init__(self, game_width, game_height, grid_location_x, grid_location_y,
        grid_width, grid_height, square_size
    ):
        self.level, self.score = 2, 0
        self.state = GAMESTATE.RUNNING

        self.height, self.width = game_height, game_width
        self.grid_location_x, self.grid_location_y = grid_location_x, grid_location_y
        self.grid_width, self.grid_height = grid_width, grid_height
        self.square_size = square_size

        self.figures, self.nextFigures = [], []
        self.velocity = 1

        self.initFigures()

        # Grid is by y then x. So grid[y][x]
        self.grid = [[None for i in range(self.grid_width)] for j in range(self.grid_height)]

    @classmethod
    def _getNextFigureId(cls) -> int:
        cls.currentFigureIndex += 1
        return cls.currentFigureIndex


    def initFigures(self):
        self.nextFigures.append(Figure.getRandomFigure(self._getNextFigureId(), self.grid_width, self.grid_height, self.square_size))
        self.nextFigures.append(Figure.getRandomFigure(self._getNextFigureId(), self.grid_width, self.grid_height, self.square_size))
        self.nextFigures.append(Figure.getRandomFigure(self._getNextFigureId(), self.grid_width, self.grid_height, self.square_size))
        self.nextFigures.append(Figure.getRandomFigure(self._getNextFigureId(), self.grid_width, self.grid_height, self.square_size))

    # new figure method
    def newFigure(self):
        nextFig: Figure = self.nextFigures.pop()

        nextFig.setX(self.grid_width//2)
        nextFig.setY(self.grid_height-4)
        nextFig.isActive = True

        self.nextFigures.append(Figure.getRandomFigure(self._getNextFigureId(), self.grid_width, self.grid_height, self.square_size))

        self.figures.append(nextFig)

    def getActiveFigure(self):
        for fig in self.figures:
            if fig.isActive:
                return fig
            
    def updateGrid(self):
        # Reset the grid
        self.grid = [[None for i in range(self.grid_width)] for j in range(self.grid_height)]
        # Add each figure's coords to the grid
        for fig in self.figures:
            for coord in fig.coordList:
                try:
                    x, y = coord[0], coord[1]
                    self.grid[y][x] = fig
                except IndexError as e:
                    continue    

    # draw method
    def draw(self, screen):
        for fig in self.figures:
            fig.draw(screen)

    def deactivate(self):
        for fg in self.figures:
            if fg.state == "stop" and fg.isActive:
                fg.isActive = False

    def checkGameState(self):
        for fig in self.figures:
            if fig.state == "stop" and fig.getTop() < 0:
                self.state = GAMESTATE.GAMEOVER

    # clear method
    def clearFullRows(self):
        rowCleared = False

        for y, row in enumerate(reversed(self.grid)):
            isRowFull = True
            for x, gridLocation in enumerate(row):
                if gridLocation is None:
                    isRowFull = False
                elif rowCleared and gridLocation is not None:
                    gridLocation.state = "start"

            if isRowFull:
                for x, fig in enumerate(row):
                    fig.remove(x, y)
                rowCleared = True

        self.updateGrid()

    # distance funnction helpers
    def distanceDownActive(self):
        activeFigure = self.getActiveFigure()
        if activeFigure is None:
            return 0

        # find minimum space open from all block in active figure
        emptySpacePerCoord = []
        for coord in activeFigure.coordList:
            # Check how many empty spaces underneath
            spacesUnder, emptySpace, empty = 0, 0, True
            y, x = coord[1], coord[0]

            while empty:
                spacesUnder += 1
                if y+spacesUnder >= self.grid_height:
                    break

                if self.grid[y+spacesUnder][x] is None or self.grid[y+spacesUnder][x] is activeFigure:
                    emptySpace = spacesUnder
                else:
                    empty = False

            emptySpacePerCoord.append(emptySpace)
        return min(emptySpacePerCoord)            
                
    def distanceLeftActive(self):
        activeFigure = self.getActiveFigure()
        if activeFigure is None:
            return 0

    def distanceRightActive(self):
        activeFigure = self.getActiveFigure()
        if activeFigure is None:
            return 0

    # move method
    def move(self):
        for fig in self.figures:
            if fig.state == "start":
                spaceLeft = self.grid_height - fig.getBottom() - 1
                enoughSpace = self.velocity < spaceLeft
                moveAmount = self.velocity if enoughSpace else spaceLeft

                if self.willCollide(fig=fig, dx=0, dy=moveAmount):
                    fig.state = "stop"
                else:
                    fig.setY(fig.y+moveAmount)

            if fig.getBottom() == self.grid_height -1:
                fig.state = "stop"

    # leftMove method
    def leftMove(self):
        for fig in self.figures:
            if fig.isActive and fig.getLeft() >= 0:
                moveAmount = -1 if fig.getLeft() > 0 else fig.getLeft()

                if self.willCollide(fig=fig, dx=moveAmount, dy=0):
                    continue
                else:
                    fig.setX(fig.x+moveAmount)

    # x:160 FigWidth: 60 ScreenWidth: 1000 Move: 840
    # rightMove method
    def rightMove(self):
        for fig in self.figures:
            if fig.isActive and fig.getRight() <= self.grid_width:
                moveAmount = 1 if (self.grid_width - fig.getRight()) > 1 else 0

                if self.willCollide(fig=fig, dx=moveAmount, dy=0):
                    continue
                else:
                    fig.setX(fig.x+moveAmount)

    # downMove method
    def downMove(self):
        for fig in self.figures:
            if fig.isActive and fig.getBottom() <= self.grid_height:
                spaceLeft = self.grid_height - fig.getBottom() - 1
                enoughSpace = self.velocity < spaceLeft
                moveAmount = self.velocity if enoughSpace else spaceLeft

                if self.willCollide(fig=fig, dx=0, dy=moveAmount):
                    continue
                else:
                    fig.setY(fig.y+moveAmount)

            if fig.getBottom() == self.grid_height -1:
                fig.state = "stop"

    # rotate method
    def rotate(self):
        for fig in self.figures:
            if fig.isActive:
                fig.rotate()
                break

    def willCollide(self, fig, dx, dy):
        """
            Check the new coordinates of the figure, and see if anything other than itself is on the grid at those locations
        """
        # Calculate the new coordinates (without actually changing them in the figure)
        newCoordList = [(coord[0]+dx, coord[1]+dy) for coord in fig.coordList]
        # Make sure none of the new coordinates already have shapes in them
        for coord in newCoordList:
            x, y = coord[0], coord[1]
            if x<0 or y<0:
                continue

            shapeAtCoord = self.grid[y][x] is not None
            thisFigAtCoord = self.grid[y][x] is fig

            if shapeAtCoord and not thisFigAtCoord:
                return True
        return False

    def start(self):
        
        size = ((self.grid_width+10)*self.square_size, self.grid_height*self.square_size)

        game_paused, menu_state = False, "main"
        font = pygame.font.SysFont("arial", 40)
        TEXT_COL = (255, 255, 255)

        # screen window
        screen = pygame.display.set_mode((size))

        # title & caption
        pygame.display.set_caption('Tetris')

        # font variables
        font = pygame.font.SysFont('arial', 40)

        # # load images
        # path = "src/Button/Images/"
        # start_img = pygame.image.load(os.path.join(os.getcwd(), path, "start_btn.png"))
        # exit_img = pygame.image.load(os.path.join(os.getcwd(), path, "exit_btn.png"))
        # resume_img = pygame.image.load(os.path.join(os.getcwd(), path, "button_resume.png"))
        # options_img = pygame.image.load(os.path.join(os.getcwd(), path, "button_options.png"))
        # quit_img = pygame.image.load(os.path.join(os.getcwd(), path, "button_quit.png"))
        # back_img = pygame.image.load(os.path.join(os.getcwd(), path, "button_back.png"))

        # # create button instances
        # start_button = Button(200, 200, start_img, 0.8)
        # exit_button = Button(200, 200, exit_img, 0.8)
        # resume_button = Button(304, 125, resume_img, 1)
        # options_button = Button(297, 250, options_img, 1)
        # quit_button = Button(336, 375, quit_img, 1)
        # back_button = Button(332, 450, back_img, 1)
            
        # game variables
        running = True
        game_tick_freq = 3
        turn = 0

         # game loop
        while running:
            moved = False
            screen.fill((52, 78, 91))

            # call draw
            self.draw(screen)

            if self.state is GAMESTATE.GAMEOVER:
                print("Game over")
                break

            # call move
            if turn % game_tick_freq == 0:
                self.move()
                moved = True

            # call deactive 
            self.deactivate()

            # call new figures
            if self.getActiveFigure() is None:
                self.newFigure()

            # check if game is paused
            if game_paused == True:
                # check menu state
                if menu_state == "main":
                    # # check buttons has been drawn
                    # if start_button.draw(screen):
                    #      # call draw
                    #     self.draw(screen)

                    #     # call move
                    #     self.move()

                    # if exit_button.draw(screen):
                    #     # quit
                    #     pygame.quit()
                    #     sys.exit(0)
                    pass

                    # draw pause screen buttons
                    if resume_button.draw(screen):
                        game_paused = False

                    if options_button.draw(screen):
                        menu_state = "options"

                    # if quit_button.draw(screen):
                    #     running = False
                    #     # quit
                    #     pygame.quit()
                    #     sys.exit(0)

                # check if the options menu is open
                if menu_state == "options":
                    if back_button.draw(screen):
                        menu_state = "main"
            
            # event handler
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == QUIT:
                        # quit
                        running = False
                        pygame.quit()
                        sys.exit(0)
                    if event.key == K_DOWN:
                        self.downMove()
                        moved = True
                    if event.key == K_LEFT:
                        self.leftMove()
                        moved = True
                    if event.key == K_RIGHT:
                        self.rightMove()
                        moved = True
                    if event.key == K_SPACE:
                        self.rotate()
                        moved = True
                    if event.key == K_ESCAPE:
                        game_paused = True

            time.sleep(.1)
            turn += 1
            if moved:
                self.updateGrid()

            self.checkGameState()

            #self.clearFullRows()

            # pygame update
            pygame.display.update()