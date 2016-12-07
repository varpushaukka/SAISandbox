from models import ManWithLaser, DIRECTIONS
from colors import WHITE, RED, GREEN, BROWN
from enum import Enum
from random import randint

TEAMS = Enum('WHITE', 'BROWN')
WINNER = TEAMS.BROWN #Define your team
class WhiteManWithLaser(ManWithLaser):
    color = WHITE
    beam = GREEN
    def run(self):
        self.move_right()

class BrownRebelScumbagWithLaser(ManWithLaser):
    color = BROWN
    beam = RED
    def run(self):
        self.set_pos(randint(0,2)*self.width,randint(0,9)*self.height)
        self.shoot()

