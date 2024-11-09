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
