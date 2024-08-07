"""
	Author: Ryan Setaruddin
	Date: August 7th, 2024
	Filename: constants.py
	Purpose: To define constant variables
"""

# define colors for background, ext messages and/or score
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

# dedine each tetrominos
I_TETROMINO = "I_TETROMINO"
O_TETROMINO = "O_TETROMINO"
T_TETROMINO = "T_TETROMINO"
L_TETROMINO = "L_TETROMINO"
J_TETROMINO = "J_TETROMINO"
S_TETROMINO = "S_TETROMINO"
Z_TETROMINO = "Z_TETROMINO"