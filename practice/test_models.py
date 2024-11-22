from Models.Figure import Figure

def test_find_figure_at_x_0():
    # Arrange
    fig1 = Figure(0, 0, 1, "I")
    fig2 = Figure(1, 0, 1, "J")
    fig3 = Figure(2, 0, 1, "K")
    figs = [fig1, fig2, fig3]

    exp_fig = fig1

    # Act
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
    fig1 = Figure(0, 0, 1, "Z")
    fig2 = Figure(1, 1, 2, "I")
    fig3 = Figure(2, 2, 3, "O")
    figs = [fig1, fig2, fig3]

    exp_fig = fig2

    # Act
    act_fig = None

    for fig in figs:
        if fig.type == "I":
            act_fig = fig

    # Assert
    assert exp_fig == act_fig
    
def test_find_active_figure():
    """
        Make a list of 3 figures, two of them should be active, and find the ones that are active.
        Follow the Arrange, Act, Assert pattern as in test_find_figure_at_x_0.
    """
    # Arrange
    fig1 = Figure(2, 0, 1, "S", True)
    fig2 = Figure(0, 1, 0, "J", True)
    fig3 = Figure(0, 0, 1, "T", False)
    figs = [fig1, fig2, fig3]

    exp_active_ct = 2

    # Act
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
    fig = Figure(200, 100, "I", True)
    
    # Act
    exp_fig = list()

    act_fig = None

    if fig.coordList:
        act_fig = fig

    # Asset
    assert exp_fig == act_fig