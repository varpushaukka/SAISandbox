from models import ManWithLaser, DIRECTIONS
from colors import WHITE, RED, GREEN
from enum import Enum

TEAMS = Enum('WHITE', 'BROWN')
WINNER = TEAMS.WHITE #Define your team
class WhiteManWithLaser(ManWithLaser):
    color = WHITE
    beam = GREEN

    def run(self):
        self.move_right()
        self.shoot()

class BrownRebelScumbagWithLaser(ManWithLaser):
    color = RED
    beam = RED
    def run(self):
        print self.ind, self.pos_x, self.pos_y
        if not self.move_left():
            if not self.move_up():
                self.move_down()