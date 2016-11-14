from models import ManWithLaser
from colors import WHITE, RED
from enum import Enum

TEAMS = Enum('WHITE', 'BROWN')
WINNER = TEAMS.WHITE #Define your team
class WhiteManWithLaser(ManWithLaser):
    color = WHITE

    def run(self):
        self.move_right()

class BrownRebelScumbagWithLaser(ManWithLaser):
    color = RED

    def run(self):
        print self.ind, self.pos_x, self.pos_y
        if not self.move_left():
            if not self.move_up():
                self.move_down()