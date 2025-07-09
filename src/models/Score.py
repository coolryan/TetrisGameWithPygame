import pygame
from dataclasses import dataclass

rowsPerLevel = 3

@dataclass
class Score:
    player_name: str 
    points: int = 0
    level: int = 1
    _rowsCleared: int = 0

    # If a certain number of rows are cleared, the level increases
    def rowCleared(self, rowsCleared: int = 1, points: int = 5):
        self._rowsCleared += rowsCleared

        if self._rowsCleared % rowsPerLevel == 0:
            self.level += 1

        self.points += points