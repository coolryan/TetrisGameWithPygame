"""
    Author: Ryan Setaruddin
    Date: Oct. 23, 2024
    Filename: Tetris.py
    Purpose: to construct a Tetris class
"""

# import libraries
import pygame, datetime, time, sys, os, json

from pygame.locals import *
from src.constants import *
from src.models.Figure import *
from src.models.Score import *

from src.buttons.Button import Button

"""
Todo next time:
Every game loop, call a method that will find all shapes that can move:

while not all(fig.canMove is not None for fig in self.figures): # While theres figures not yet validated to move
    for fig in self.figures:
        if noShapesUnder and notAtBottom:
            fig.canMvoe = True
        elif atBottom or (shapeUnder.canMove is False):
            fig.canMove = False
"""

# class TetrisGame
class TetrisGame:
    # Class state
    currentFigureIndex = 0

    """constructor"""
    def __init__(self, game_width, game_height, grid_location_x, grid_location_y,
        grid_width, grid_height, square_size, player_name
    ):
        self.score = Score(player_name, 1)
        self.state = GAMESTATE.RUNNING

        self.height, self.width = game_height, game_width
        self.grid_location_x, self.grid_location_y = grid_location_x, grid_location_y
        self.grid_width, self.grid_height = grid_width, grid_height
        self.square_size = square_size

        self.figures, self.nextFigures = [], []
        self.velocity = 1
        self.sleep_time = .2

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
        nextFig: Figure = self.nextFigures[0]
        self.nextFigures.remove(nextFig)

        nextFig.setX(self.grid_width//2)
        nextFig.setY(-4)
        nextFig.isActive = True
        
        upcomingFigure: Figure = self.nextFigures[0]
        x, y = self.next_surface.get_bounding_rect().topleft
        upcomingFigure.setX(0)
        upcomingFigure.setY(0)
        
        self.upcomingFigure = upcomingFigure
        self.nextFigures.append(Figure.getRandomFigure(self._getNextFigureId(), self.grid_width, self.grid_height, self.square_size))
        self.figures.append(nextFig)

    def getActiveFigure(self):
        for fig in self.figures:
            if fig.isActive:
                return fig

    def markFiguresCanFall(self):
        """
        go through every figure on the board
        and mark which figures can fall or not
        """
        for fig in self.figures:
            fig.canFall = CANFALL.UNDEFINED

        # Todo: This seems to get stuck sometimes
        max_iterations = 100
        iterations = 0
        while any([fig.canFall == CANFALL.UNDEFINED for fig in self.figures]) and iterations < max_iterations:
            for fig in [fig for fig in self.figures if fig.canFall == CANFALL.UNDEFINED]:
                fig.canFall = self.canFall(fig)
            iterations += 1

    def canFall(self, fig: Figure) -> CANFALL:
        # a figure can fall if one or two scenarios are true:
        # * if there is nothing under it and its not in the bottom of the screen.
        # * all shapes under it are also falling.
        # left off here. returns a CANFALL enum value
        figuresUnder = self.getFiguresUnder(fig, 0, 1)
        if fig.getBottom() >= self.grid_height -1:
            return CANFALL.FALSE
        elif len(figuresUnder) == 0:
            return CANFALL.TRUE
        #TODO possibly bug
        elif len([otherFigs for otherFigs in figuresUnder if otherFigs.canFall != CANFALL.TRUE]) == 0:
            return CANFALL.TRUE
        elif len([otherFigs for otherFigs in figuresUnder if otherFigs.canFall == CANFALL.FALSE]) > 0:
            return CANFALL.FALSE
        else:
            return CANFALL.UNDEFINED
            
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
            # fig.draw(screen)
            fig.draw(self.grid_surface)

    def deactivate(self):
        for fig in self.figures:
            if self.canFall(fig) == CANFALL.FALSE and fig.isActive:
                fig.isActive = False

    def checkGameState(self):
        # Check if any figure is at the top of the grid, if so gameover
        for fig in self.figures:
            if self.canFall(fig) == CANFALL.FALSE and fig.getTop() < 0:
                
                self.state = GAMESTATE.GAMEOVER

    # clear method
    def clearFullRows(self):
        for y, row in enumerate(reversed(self.grid)):
            isRowFull = self.getIsRowFull(y, row)
            
                # Lets set the rows above emptied row to start so they fall down
                # elif rowCleared and gridLocation is not None:
                #     gridLocation.state = "start"

            if isRowFull:
                print("Row full")
                for x, fig in enumerate(row):
                    coord_x = x
                    coord_y = self.grid_height - 1 - y
                    fig.remove(coord_x, coord_y)

                self.score.rowCleared()

                self.sleep_time = {
                    1: .2,
                    2: .18,
                    3: .16,
                    4: .15,
                    5: .14,
                }[self.score.level]

                isRowFull = False

                # if len(fig.coordList) == 0:
                #     self.figures.remove(fig)

        figures = []
        for fig in self.figures:
            if len(fig.coordList) > 0:
                figures.append(fig)
        self.figures = figures

        self.updateGrid()

    def getIsRowFull(self, y, row) -> bool:
        isRowFull = True
        for _, gridLocation in enumerate(row):
            if gridLocation is None:
                isRowFull = False
        return isRowFull

    def checkFloatingRows(self):
        # Check which shapes can fall
        for y, row in enumerate(reversed(self.grid)):
            allEmpty = True
            for x, gridLocation in enumerate(row):
                if gridLocation is not None:
                    allEmpty = False
            if allEmpty:
                for x, gridLocation in enumerate(row):
                    if gridLocation:
                        # gridLocation.state = "start"
                        pass


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
            if self.canFall(fig) == CANFALL.TRUE:
                spaceLeft = self.grid_height - fig.getBottom() - 1
                enoughSpace = self.velocity < spaceLeft
                moveAmount = self.velocity if enoughSpace else spaceLeft

                if self.willCollide(fig=fig, dx=0, dy=moveAmount):
                    continue
                else:
                    fig.setY(fig.y+moveAmount)

            if fig.getBottom() == self.grid_height -1:
                continue

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
            if fig.isActive and fig.getRight() < self.grid_width:
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
                continue

    # rotate method
    # Todo: Fix bug where if rotating makes part of the shape go off screen, crashes
    def rotate(self):
        for fig in self.figures:
            if fig.isActive:
                fig.rotate()
                if fig.getLeft() < 0 or fig.getRight() >= self.grid_width:
                    fig.unrotate()
                break

    def willCollide(self, fig, dx, dy):
        """
            Check the new coordinates of the figure, and see if anything other than itself is on the grid at those locations
        """
        return len(self.getFiguresUnder(fig, dx, dy)) > 0
    
    def getFiguresUnder(self, fig: Figure, dx, dy):
        """
            Check the new coordinates of the figure, and returns anything other than itself on the grid at those locations
        """
        if fig.getBottom() == self.grid_height -1:
            return set()

        # Calculate the new coordinates (without actually changing them in the figure)
        newCoordList = [(coord[0]+dx, coord[1]+dy) for coord in fig.coordList]
        # Make sure none of the new coordinates already have shapes in them
        figuresUnder = set()
        for coord in newCoordList:
            x, y = coord[0], coord[1]
            if x<0 or y<0:
                continue

            shapeAtCoord = self.grid[y][x] is not None
            thisFigAtCoord = self.grid[y][x] is fig

            if shapeAtCoord and not thisFigAtCoord:
                figuresUnder.add(self.grid[y][x])
        return figuresUnder
    
    def display_score(self, screen):
        font = pygame.font.SysFont('Calibri', 25, True, False)
        scoreText = font.render("Score: " + str(self.score.points), True, BLACK)
        textRect = scoreText.get_rect()
        textRect.topleft = (10, 10)
        screen.blit(scoreText, textRect)

    def display_level(self, screen):
        font = pygame.font.SysFont('Calibri', 25, True, False)
        levelText = font.render("Level: " + str(self.score.level), True, BLACK)
        textRect = levelText.get_rect()
        textRect.topleft = (10, 35)
        screen.blit(levelText, textRect)

    def game_over(self):
        # variables
        name = self.score.player_name
        highScore = self.score.points
        level = self.score.level
        currentDateTime = datetime.datetime.now()
        formattedDateTime = currentDateTime.strftime("%Y-%m-%d %H:%M:%S")
        
        # your game data
        game_data = {
            "name": name,
            "score": highScore,
            "level": level,
            "date": formattedDateTime
        }

        # define the data folder & file path
        data_folder = "data"
        file_name = "save_game.json"
        file_path = os.path.join(data_folder, file_name)

        # create the data folder if it doesn't exist
        if not os.path.exists(file_path):
            os.makedirs(data_folder)

        # write the JSON data to the file                         
        # loaded the game data
        try:
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    loaded_data = json.load(file)
            else:
                loaded_data = []
            loaded_data.append(game_data)

            with open(file_path, "w") as file:
                json.dump(loaded_data, file, indent=4)

            print(f"Wrote game data:", loaded_data )
        
        except FileNotFoundError:
            print(f"No Saved game found found: {file_path}. Starting new game.")

        except json.JSONDecodeError:
            print(f"Error: Saved game file {file_path}' is corrupted. Starting new game.")

    def start(self):
        size = ((self.grid_width+10)*self.square_size, self.grid_height*self.square_size)

        game_paused, menu_state = False, "main"
        TEXT_COL = (255, 255, 255)

        # screen window
        screen = pygame.display.set_mode((size))

        # title & caption
        pygame.display.set_caption('Tetris')

        # font variables
        font = pygame.font.SysFont('arial', 40)

        # load images
        path = "resources/button/images"
        start_img = pygame.image.load(os.path.join(os.getcwd(), path, "start_btn.png"))
        exit_img = pygame.image.load(os.path.join(os.getcwd(), path, "exit_btn.png"))
        # resume_img = pygame.image.load(os.path.join(os.getcwd(), path, "button_resume.png"))
        # options_img = pygame.image.load(os.path.join(os.getcwd(), path, "button_options.png"))
        # quit_img = pygame.image.load(os.path.join(os.getcwd(), path, "button_quit.png"))
        # back_img = pygame.image.load(os.path.join(os.getcwd(), path, "button_back.png"))

        # create button instances
        start_button = Button(300, 200, start_img, 0.8)
        exit_button = Button(500, 200, exit_img, 0.8)
        # resume_button = Button(304, 125, resume_img, 1)
        # options_button = Button(297, 250, options_img, 1)
        # quit_button = Button(336, 375, quit_img, 1)
        # back_button = Button(332, 450, back_img, 1)
            
        # game variables
        running = True
        game_tick_freq = 3
        turn = 0

        # rect = pygame.Rect(x, y, width, height)
        # pygame.draw.rect(screen, self.color, rect)

        # game loop
        while running:
            moved = False
            
            # self.height, self.width = game_height, game_width
            # self.grid_location_x, self.grid_location_y = grid_location_x, grid_location_y
            # self.grid_width, self.grid_height = grid_width, grid_height
            # self.square_size = square_size

            screen.fill(BG_COLOR) # Gives background color
            # Draw grid
            net_grid_width = self.grid_width * self.square_size
            net_grid_height = self.grid_height * self.square_size

            grid_x, gird_y = self.grid_location_x * self.square_size, self.grid_location_y * self.square_size
            grid_rec = pygame.Rect(grid_x, gird_y, net_grid_width, net_grid_height)

            self.grid_surface = screen.subsurface(grid_rec)
            self.grid_surface.fill(GRID_COLOR)

            next_rect = pygame.Rect(780, 20, 200, 200)
            self.next_surface = screen.subsurface(next_rect)
            self.next_surface.fill(GRID_COLOR)
            # pygame.draw.rect(screen, GRID_COLOR, self.grid_surface)

            cell_size = self.square_size  # or whatever size your cells are
            grid_color = (50, 50, 50)  # a dark gray or any color you like

            # Draw vertical lines
            for x in range(0, net_grid_width, cell_size):
                pygame.draw.line(self.grid_surface, grid_color, (x, 0), (x, net_grid_height))

            # Draw horizontal lines
            for y in range(0, net_grid_height, cell_size):
                pygame.draw.line(self.grid_surface, grid_color, (0, y), (net_grid_width, y))

            # call draw
            self.draw(screen)

            if self.state is GAMESTATE.GAMEOVER:
                self.game_over()
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
                    # check buttons has been drawn
                    if start_button.draw(screen):
                        # call draw
                        self.draw(screen)

                        # call move
                        self.move()

                    if exit_button.draw(screen):
                        # quit
                        pygame.quit()
                        sys.exit(0)

                    # # draw pause screen buttons
                    # if resume_button.draw(screen):
                    #     game_paused = False

                    # if options_button.draw(screen):
                    #     menu_state = "options"

                    # if quit_button.draw(screen):
                    #     running = False
                    #     # quit
                    #     pygame.quit()
                    #     sys.exit(0)

                # check if the options menu is open
                # if menu_state == "options":
                #     if back_button.draw(screen):
                #         menu_state = "main"

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

            time.sleep(self.sleep_time)
            turn += 1
            if moved:
                self.updateGrid()
                self.markFiguresCanFall()

            self.checkGameState()

            self.clearFullRows()
            self.checkFloatingRows()

            self.display_score(screen)
            self.display_level(screen)
            if hasattr(self, 'upcomingFigure'):
                self.upcomingFigure.draw(self.next_surface)

            # pygame update
            pygame.display.update()
