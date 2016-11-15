from models import ManWithLaser, DIRECTIONS
from colors import WHITE, RED, GREEN, BROWN
from enum import Enum

TEAMS = Enum('WHITE', 'BROWN')
WINNER = TEAMS.WHITE #Define your team
class WhiteManWithLaser(ManWithLaser):
    color = WHITE
    beam = GREEN
    def run(self):
        self.move_right()

class BrownRebelScumbagWithLaser(ManWithLaser):
    color = BROWN
    beam = RED
    def run(self):
        self.move_left()