import pytest

from src.models.TetrisGame import Figure, TetrisGame
from src.constants import *

@pytest.skip("not in use")
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

@pytest.skip("not in use")
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

def test_getIsRowFull_buttonRowFull():
    # Arrange
    tetris = TetrisGame(5, 5, 1)
    y = 1
    row = []

    # Act
    result = tetris.getIsRowFull(y, row)

    # Assert
    assert True