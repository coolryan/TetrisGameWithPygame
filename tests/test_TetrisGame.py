from typing import Optional
import pytest
from pytest_mock import MockerFixture

from src.models.TetrisGame import Figure, TetrisGame
from src.constants import *

@pytest.fixture
def tetris_game() -> TetrisGame:
    game_width, game_height = 20, 25
    grid_location_x, grid_location_y = 5, 0

    # Size in grid
    grid_width, grid_height, square_size = 10, 20, 50

    tetris = TetrisGame(game_width, game_height, 
                        grid_location_x, grid_location_y, 
                        grid_width, grid_height, square_size, player_name="test")
    return tetris

@pytest.fixture
def test_empty_grid() -> list[list[Optional[Figure]]]:
    # Grid is by y then x. So grid[y][x]
    grid_width = 10
    grid_height = 20
    grid = [[None for i in range(grid_width)] for j in range(grid_height)]
    return grid


@pytest.fixture
def test_figure():
    isActive = False
    newFig = Figure(1, 0, 0, 1, O_TETROMINO, isActive)
    return newFig

# This is represenation of a grid, a is a shape, b is another shape, _ means empty
# _ _ _ _ _
# _ _ _ _ _
# _ _ _ _ b
# a a a a b
@pytest.fixture
def test_full_bottom_grid():
    # Grid is by y then x. So grid[y][x]
    # y=0 will be the top, y=height-1 will be the bottom
    grid_width = 10
    grid_height = 20
    grid = [[None for i in range(grid_width)] for j in range(grid_height)]

    figA = Figure(id=0, x=0, y=0, size=50, figureType=O_TETROMINO, isActive=False)
    figB = Figure(id=1, x=9, y=0, size=50, figureType=T_TETROMINO, isActive=False)
    # Fill the bottom with all figA, but last column with figB
    last_row = [figA for _ in range(grid_width)]
    last_row[grid_width-1] = figB
    grid[grid_height-1] = last_row

    return grid


@pytest.mark.skip("not in use")
def test_distanceDownActive_none_below():
    # Arrange
    tetris = TetrisGame(5, 5, 1)
    isActive = True
    newFig = Figure(1, 0, 0, 1, O_TETROMINO, isActive)
    tetris.figures.append(newFig)

    # Act
    result = tetris.distanceDownActive()

    # Assert
    assert result == 3

@pytest.mark.skip("not in use")
def test_distanceDownActive_another_below():
    # Arrange
    tetris = TetrisGame(5, 5, 1)
    isActive = True
    newFig = Figure(1, 0, 0, 1, O_TETROMINO, isActive)
    tetris.figures.append(newFig)
    anotherFig = Figure(2, 0, 4, 1, O_TETROMINO, False)
    tetris.figures.append(anotherFig)

    # Act
    result = tetris.distanceDownActive()

    # Assert
    assert result == 1

def test_getIsRowFull_RowFull(tetris_game: TetrisGame):
    # Arrange
    y = 1
    isActive = False
    row_of_figs = [Figure(id, 0, 0, 1, O_TETROMINO, isActive) for id in range(tetris_game.width)]

    # Act
    result = tetris_game.getIsRowFull(y, row_of_figs)

    # Assert
    assert result is True

def test_getIsRowFull_RowOneEmpty(tetris_game: TetrisGame):
    # Arrange
    y = 1
    isActive = False
    row_of_figs = [Figure(id, 0, 0, 1, O_TETROMINO, isActive) for id in range(tetris_game.width)]
    row_of_figs[0] = None

    # Act
    result = tetris_game.getIsRowFull(y, row_of_figs)

    # Assert
    assert result is False

def test_getIsRowFull_RowFullyEmpty(tetris_game: TetrisGame):
    # Arrange
    row_of_figs = [None for _ in range(tetris_game.width)]
    y = 1

    # Act
    result = tetris_game.getIsRowFull(y, row_of_figs)

    # Assert
    assert result is False

def test_clearFullRows_bottomRowFull(mocker: MockerFixture, tetris_game: TetrisGame, test_full_bottom_grid: list[list[Optional[Figure]]]):
    # Arrange
    # Set the grid up for the test
    tetris_game.grid = test_full_bottom_grid

    # Act
    tetris_game.clearFullRows()

    # Assert
    assert all(item is None for item in tetris_game.grid[tetris_game.grid_height-1])


def test_clearFullRows_second_from_bottom_full(
    tetris_game: TetrisGame,
    test_empty_grid: list[list[Optional[Figure]]]
):
    # Arrange
    # Set the grid up for the test
    oneUpY = tetris_game.grid_height - 2
    tetris_game.grid = test_empty_grid
    figO1 = Figure(id=0, x=0, y=oneUpY, size=50, figureType=O_TETROMINO, isActive=False)
    figO2 = Figure(id=0, x=2, y=oneUpY, size=50, figureType=O_TETROMINO, isActive=False)
    figO3 = Figure(id=0, x=4, y=oneUpY, size=50, figureType=O_TETROMINO, isActive=False)
    figT1 = Figure(id=0, x=6, y=oneUpY, size=50, figureType=T_TETROMINO, isActive=False)
    figI1 = Figure(id=1, x=9, y=tetris_game.grid_height-4, size=50, figureType=I_TETROMINO, isActive=False)
    tetris_game.figures = [figO1, figO2, figO3, figT1, figI1]
    # Now lets fill the grid out  
    tetris_game.updateGrid()
    # Make sure they're not clear right now
    assert not all(item is None for item in tetris_game.grid[tetris_game.grid_height-2])
    assert not all(item is None for item in tetris_game.grid[tetris_game.grid_height-1])

    # Act
    tetris_game.clearFullRows()

    # Assert
    assert all(item is None for item in tetris_game.grid[tetris_game.grid_height-2])
    assert not all(item is None for item in tetris_game.grid[tetris_game.grid_height-1])

def test_clearFullRows_bottomTwoRows(
        tetris_game: TetrisGame,
        test_empty_grid: list[list[Optional[Figure]]]
):
    # Arrange
    # Set the grid up for the test
    oneUpY = tetris_game.grid_height - 2
    tetris_game.grid = test_empty_grid
    figO1 = Figure(id=0, x=0, y=oneUpY, size=50, figureType=O_TETROMINO, isActive=False)
    figO2 = Figure(id=0, x=2, y=oneUpY, size=50, figureType=O_TETROMINO, isActive=False)
    figO3 = Figure(id=0, x=4, y=oneUpY, size=50, figureType=O_TETROMINO, isActive=False)
    figO4 = Figure(id=0, x=6, y=oneUpY, size=50, figureType=O_TETROMINO, isActive=False)
    figO5 = Figure(id=1, x=8, y=oneUpY, size=50, figureType=O_TETROMINO, isActive=False)
    tetris_game.figures = [figO1, figO2, figO3, figO4, figO5]
    # Now lets fill the grid out
    tetris_game.updateGrid()
    # Make sure they're not clear right now
    assert not all(item is None for item in tetris_game.grid[tetris_game.grid_height-2])
    assert not all(item is None for item in tetris_game.grid[tetris_game.grid_height-1])

    # Act
    tetris_game.clearFullRows()

    # Assert
    assert all(item is None for item in tetris_game.grid[tetris_game.grid_height-2])
    assert all(item is None for item in tetris_game.grid[tetris_game.grid_height-1])

def test_clearFullRows_bottomTwoUpRows(
        tetris_game: TetrisGame,
        test_empty_grid: list[list[Optional[Figure]]]
):
    # Arrange
    # Set the grid up for the test
    oneUpY = tetris_game.grid_height - 2
    twoUpY = tetris_game.grid_height - 3
    threeUpY = tetris_game.grid_height - 4
    tetris_game.grid = test_empty_grid
    
    figO1 = Figure(id=0, x=0, y=twoUpY, size=50, figureType=O_TETROMINO, isActive=False)
    figT1 = Figure(id=0, x=2, y=twoUpY, size=50, figureType=T_TETROMINO, isActive=False)
    figT2 = Figure(id=0, x=5, y=twoUpY, size=50, figureType=T_TETROMINO, isActive=False)
    figO2 = Figure(id=0, x=8, y=threeUpY, size=50, figureType=O_TETROMINO, isActive=False)
    figI1 = Figure(id=1, x=8, y=oneUpY, size=50, figureType=I_TETROMINO, isActive=False)
    figI2 = Figure(id=1, x=8, y=oneUpY, size=50, figureType=I_TETROMINO, isActive=False)
    figO3 = Figure(id=0, x=8, y=oneUpY, size=50, figureType=O_TETROMINO, isActive=False)
    
    figI1.rotate()
    figI1.setX(0)
    figI1.setY(tetris_game.grid_height)
    
    figI2.rotate()
    figI2.setX(4)
    figI2.setY(tetris_game.grid_height)

    tetris_game.figures = [figO1, figT1, figT2, figO2, figI1, figI2, figO3]

    # Now lets fill the grid out
    tetris_game.updateGrid()
    # Make sure they're not clear right now
    assert not all(item is None for item in tetris_game.grid[tetris_game.grid_height-3])
    assert not all(item is None for item in tetris_game.grid[tetris_game.grid_height-2])
    assert not all(item is None for item in tetris_game.grid[tetris_game.grid_height-1])

    # Act
    tetris_game.clearFullRows()

    # Assert
    assert all(item is None for item in tetris_game.grid[tetris_game.grid_height-3])
    assert not all(item is None for item in tetris_game.grid[tetris_game.grid_height-2])
    assert all(item is None for item in tetris_game.grid[tetris_game.grid_height-1])