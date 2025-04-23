import pygame
from dataclasses import dataclass

@dataclass
class Score:
    player_name: str 
    points: int = 0
    level: int = 1