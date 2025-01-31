from Models.Figure import Figure
from constants import *

def test_find_figure_at_x_0():
    # Arrange
    fig1 = Figure(0, 0, 0, 1, I_TETROMINO)
    fig2 = Figure(1, 1, 0, 1, J_TETROMINO)
    fig3 = Figure(2, 2, 0, 1, L_TETROMINO)
    figs = [fig1, fig2, fig3]

    # Act
    exp_fig = fig1
    act_fig = None

    for fig in figs:
        if fig.x == 0:
            act_fig = fig
            break
    
    # Assert
    assert exp_fig == act_fig


def test_find_type_I_figure():
    """
        Make a list of 3 figures, and find the one of type "I".
        Follow the Arrange, Act, Assert pattern as in test_find_figure_at_x_0.
    """
    # Arrange
    fig1 = Figure(0, 0, 0, 1, Z_TETROMINO)
    fig2 = Figure(1, 1, 1, 2, I_TETROMINO)
    fig3 = Figure(2,2, 2, 3, O_TETROMINO)
    figs = [fig1, fig2, fig3]

    # Act
    exp_fig = fig2
    act_fig = None

    for fig in figs:
        if fig.type == I_TETROMINO:
            act_fig = fig

    # Assert
    assert exp_fig == act_fig
    
def test_find_active_figure():
    """
        Make a list of 3 figures, two of them should be active, and find the ones that are active.
        Follow the Arrange, Act, Assert pattern as in test_find_figure_at_x_0.
    """
    # Arrange
    fig1 = Figure(1, 2, 0, 1, S_TETROMINO, True)
    fig2 = Figure(2, 0, 1, 0, J_TETROMINO, True)
    fig3 = Figure(3, 0, 0, 1, T_TETROMINO, False)
    figs = [fig1, fig2, fig3]

    # Act
    exp_active_ct = 2
    act_active = 0

    for fig in figs:
        if fig.isActive:
            act_active += 1

    # Assert
    assert act_active == exp_active_ct 


def test_initFigure_I():
    """
        Test creating an I_TETROMINO figure. Make sure the created figure has 4 items in its coordList.
    """
    # Arrange 
    # Act
    fig = Figure(1, 200, 200, 100, I_TETROMINO)

    # Asset
    assert len(fig.coordList) == 4


def test_getrandomFigure():
    """
        test that generates two differment random objects
    """
    # Arrange
    maxX = 100
    maxY = 100
    size = 300

    # Act
    fig1 = Figure.getRandomFigure(1, maxX, maxY, size)
    fig2 = Figure.getRandomFigure(2, maxX, maxY, size)

    # Asset
    assert fig1 != fig2