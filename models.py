from colors import BLACK, GRAY, RED
from enum import Enum
DIRECTIONS = Enum('LEFT', 'RIGHT', 'UP', 'DOWN')

class Shot(object):

    def __init__(self, color, x, y, direction, ind):
        self.color = color
        self.x = x
        self.y = y
        self.direction = direction
        self.shooter_ind = ind

    def get_object(self):
        return self.x, self.y, self.color, self.direction, self.shooter_ind

    def get_pos(self):
        return  self.x, self.y

class Model(object):
    pos_x = 0
    pos_y = 0
    width = 0
    height = 0
    color = BLACK
    shootable = False

    def __init__(self, x,y,w,h, ind):
        self.set_scale(h, w)
        self.set_pos(x,y)
        self.ind = ind

    def set_pos(self, x, y):
        print x,y
        self.pos_x = int(x)
        self.pos_y = int(y)

    def get_pos(self):
        return self.pos_x, self.pos_y

    def set_scale(self, h, w):
        self.width = int(w)
        self.height = int(h)

    def get_scale(self):
        return self.height, self.width

    def get_object(self):
        x,y = self.get_pos()
        h,w = self.get_scale()
        return x, y, h, w, self.color

    def is_shootable(self):
        return self.shootable

class Block(Model):
    color = GRAY
    shootable = False

class ManWithLaser(Model):
    color = RED
    beam = RED
    shootable = True
    last_facing = DIRECTIONS.LEFT
    prev_pos_x = None
    prev_pos_y = None

    def set_blocks(self, blocks):
        self.blocks = blocks

    def set_shots(self, shots):
        self.shots = shots

    def run(self):
        pass

    def shoot(self):
        s = Shot(self.beam, self.pos_x, self.pos_y, self.last_facing, self.ind)
        self.shots.append(s)


    def move_left(self):
        self._update_prev_pos()
        self.last_facing = DIRECTIONS.LEFT
        next_pos_x = self.pos_x - self.width
        if next_pos_x <= 0:
            next_pos_x = 0
        next_pos_y = self.pos_y
        if not self._check_blocks(next_pos_x, next_pos_y):
            return False
        self.set_pos(next_pos_x, next_pos_y)
        return True

    def _update_prev_pos(self):
        self.prev_pos_x = self.pos_x
        self.prev_pos_y = self.pos_y

    def move_right(self):
        self._update_prev_pos()
        self.last_facing = DIRECTIONS.RIGHT
        next_pos_x = self.pos_x + self.width
        if next_pos_x >= self.width*9:
            next_pos_x = self.width*9
        next_pos_y = self.pos_y
        if not self._check_blocks(next_pos_x, next_pos_y):
            return False
        self.set_pos(next_pos_x, next_pos_y)
        return True

    def move_up(self):
        self._update_prev_pos()
        self.last_facing = DIRECTIONS.UP
        next_pos_y = self.pos_y - self.height
        if next_pos_y <= 0:
            next_pos_y = 0
        next_pos_x = self.pos_x
        if not self._check_blocks(next_pos_x, next_pos_y):
            return False
        self.set_pos(next_pos_x, next_pos_y)
        return True

    def move_down(self):
        self._update_prev_pos()
        self.last_facing = DIRECTIONS.DOWN
        next_pos_y = self.pos_y + self.height
        if next_pos_y >= self.height*9:
            next_pos_y = self.height*9
        next_pos_x = self.pos_x
        if not self._check_blocks(next_pos_x, next_pos_y):
            return False
        self.set_pos(next_pos_x, next_pos_y)
        return True


    def _check_blocks(self, next_pos_x, next_pos_y):
        for b in self.blocks:
            x, y = b.get_pos()
            if x == next_pos_x and y == next_pos_y:
                return False
        return True