from src.Models.Tetris import Figure, Tetris
from src.constants import *

def test_distanceDownActive_none_below():
    # Arrange
    tetris = Tetris(5, 5, 1)
    isActive = True
    newFig = Figure(1, 0, 0, 1, O_TETROMINO, isActive)
    tetris.figures.append(newFig)

    # Act
    result = tetris.distanceDownActive()

    # Assert
    assert result == 3

def test_distanceDownActive_another_below():
    # Arrange
    tetris = Tetris(5, 5, 1)
    isActive = True
    newFig = Figure(1, 0, 0, 1, O_TETROMINO, isActive)
    tetris.figures.append(newFig)
    anotherFig = Figure(2, 0, 4, 1, O_TETROMINO, False)
    tetris.figures.append(anotherFig)

    # Act
    result = tetris.distanceDownActive()

    # Assert
    assert result == 1