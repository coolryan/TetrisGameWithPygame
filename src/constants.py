"""
    Author: Ryan Setaruddin
    Date: August 7th, 2024
    Filename: constants.py
    Purpose: To define constant variables
"""

from enum import StrEnum

class GAMESTATE(StrEnum):
    RUNNING = "RUNNING"
    GAMEOVER = "GAMEOVER"
    GAMEPAUSED = "GAMEPAUSED"

# define colors for background, ext messages and/or score
TEXT_COL = (255, 255, 255)
BLACK, WHITE, GRAY = (0, 0, 0), (255, 255, 255), (128, 128, 128)

# define colores for each tetrominos
COLORS = (
    (128, 128, 128), 
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),     
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122)
)

# define each tetrominos
I_TETROMINO = "I_TETROMINO"
O_TETROMINO = "O_TETROMINO"
T_TETROMINO = "T_TETROMINO"
L_TETROMINO = "L_TETROMINO"
J_TETROMINO = "J_TETROMINO"
S_TETROMINO = "S_TETROMINO"
Z_TETROMINO = "Z_TETROMINO"

# offsets for shape coordinates
SHAPE_OFFSETS = {
    I_TETROMINO: [
        [(0,0), (0,1), (0,2), (0,3)], # RotationIndex 0
        [(0,0), (1,0), (2,0), (3,0)], # RotationIndex 1
        [(0,0), (0,1), (0,2), (0,3)], # RotationIndex 2
        [(0,0), (1,0), (2,0), (3,0)]  # RotationIndex 3
    ],
    T_TETROMINO: [
        [(0,0), (1,0), (2,0), (1,1)],
        [(1,0), (1,1), (1,2), (0,1)],
        [(0,1), (1,1), (2,1), (1,0)],
        [(1,0), (1,1), (1,2), (2,1)]
    ],
    O_TETROMINO: [
        [(0,0), (1,0), (0,1), (1,1)],
        [(0,0), (1,0), (0,1), (1,1)],
        [(0,0), (1,0), (0,1), (1,1)],
        [(0,0), (1,0), (0,1), (1,1)]
    ],
    L_TETROMINO: [
        [(0,0), (0,1), (0,2), (1,2)],
        [(0,0), (1,0), (2,0), (0,1)],
        [(0,0), (1,0), (1,1), (1,2)],
        [(2,0), (0,1), (1,1), (2,1)]
    ],
    J_TETROMINO: [
        [(1,0), (1,1), (1,2), (0,2)],
        [(0,0), (0,1), (1,1), (2,1)],
        [(1,0), (2,0), (1,1), (1,2)],
        [(0,0), (1,0), (2,0), (2,1)]
    ],
    S_TETROMINO: [
        [(1,0), (2,0), (0,1), (1,1)],
        [(0,0), (0,1), (1,1), (1,2)],
        [(1,0), (2,0), (0,1), (1,1)],
        [(0,0), (0,1), (1,1), (1,2)]
    ],
    Z_TETROMINO: [
        [(0,0), (1,0), (1,1), (2,1)],
        [(2,0), (1,1), (2,1), (1,2)],
        [(0,0), (1,0), (1,1), (2,1)],
        [(2,0), (1,1), (2,1), (1,2)]
    ]
}

# offsets for shape colors
SHAPE_COLORS = {
    I_TETROMINO: COLORS[0],
    T_TETROMINO: COLORS[1],
    O_TETROMINO: COLORS[2],
    L_TETROMINO: COLORS[3],
    J_TETROMINO: COLORS[4],
    S_TETROMINO: COLORS[5],
    Z_TETROMINO: COLORS[6]
}