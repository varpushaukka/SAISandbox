import pygame
import random
from colors import WHITE, BLACK, BLUE
from models import Block, DIRECTIONS
from challenge import WhiteManWithLaser, BrownRebelScumbagWithLaser, TEAMS, WINNER

TILE_WIDTH = 40
TILE_HEIGHT = 40
LASER_LENGTH = 20
MAP_HEIGHT = 10
MAP_WIDTH = 10
MAX_BLOCKS = 4
BLOCK_ROWS = [3,4, 5]
MAX_WHITE = 4
MAX_BROWN = 3

class Game(object):
    # Set the height and width of the screen



    pygame.display.set_caption("Example code for the draw module")

    def __init__(self, size=None):
        self.screen = pygame.display.set_mode(size)
        self.map = []
        self.tile_width = TILE_WIDTH
        self.tile_height = TILE_HEIGHT
        self.blocks = []
        self.whites = []
        self.browns = []
        self.shots = []
        self.already_shot = []
        for x in range(MAP_WIDTH):
            self.map.append([0]*MAP_HEIGHT)

        for row in BLOCK_ROWS:
            for _ in range(0, MAX_BLOCKS):
                cell = random.choice(range(0, MAP_WIDTH))
                x = row * self.tile_width
                y = cell * self.tile_height
                b = Block(x,y,self.tile_width, self.tile_height, len(self.blocks)+1)
                self.blocks.append(b)


        for _ in range(0, MAX_WHITE):
            cell = random.choice(range(0, MAP_WIDTH))
            x = 0
            y = cell * self.tile_height
            w = WhiteManWithLaser(x,y, self.tile_width, self.tile_height, len(self.whites)+1)
            w.set_blocks(self.blocks)
            w.set_shots(self.shots)
            self.whites.append(w)

        for _ in range(0, MAX_BROWN):
            cell = random.choice(range(0, MAP_WIDTH))
            x = 9*self.tile_width
            y = cell * self.tile_width
            b = BrownRebelScumbagWithLaser(x, y, self.tile_width, self.tile_height, len(self.browns) + 1)
            b.set_blocks(self.blocks)
            b.set_shots(self.shots)
            self.browns.append(b)



    def main(self):

        clock = pygame.time.Clock()

        # Loop until the user clicks the close button.
        done = False
        while not done:

            # This limits the while loop to a max of 10 times per second.
            # Leave this out and we will use all CPU we can.
            clock.tick(1)

            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop

            # All drawing code happens after the for loop and but
            # inside the main while done==False loop.

            # Clear the screen and set the screen background
            self.screen.fill(BLACK)
            self.shots = []
            # Draw a rectangle outline
            #Draw blocks
            for block in self.blocks:
                x,y,w,h,c = block.get_object()
                pygame.draw.rect(self.screen, c, [x, y, w, h])


            for white in self.whites:
                if white:
                    white.set_shots(self.shots)
                    if WINNER == TEAMS.WHITE:
                        white.run()
                    x,y,w,h,c = white.get_object()
                    pygame.draw.rect(self.screen, c, [x, y, w, h])

            for brown in self.browns:
                if brown:
                    brown.set_shots(self.shots)
                    if WINNER == TEAMS.BROWN:
                        brown.run()
                    x,y,w,h,c = brown.get_object()
                    pygame.draw.rect(self.screen, c, [x, y, w, h])

            self.already_shot = []
            for shot in self.shots:
                #pygame.draw.line(screen, GREEN, [0, 0], [50,30], 5)
                self._draw_shot(shot)
                self._check_shot(shot)

            # Go ahead and update the screen with what we've drawn.
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()
            browns_alive = self._check_alive(self.browns)
            whites_alive = self._check_alive(self.whites)
            if not browns_alive or not whites_alive:
                done = True
                if not browns_alive and WINNER == TEAMS.WHITE:
                    print "you won"
                elif not whites_alive and WINNER == TEAMS.BROWN:
                    print "you won"
                else:
                    print "You lost"
        # Be IDLE friendly
        pygame.quit()

    def _draw_shot(self, shot):
        start_x, start_y, color, dir, ind = shot.get_object()
        shot_info = "%d%d%d" % (ind, start_x, start_y)
        if not shot_info in self.already_shot:
            self.already_shot.append(shot_info)
            end_x = start_x
            end_y = start_y
            if dir == DIRECTIONS.UP:
                end_y -= TILE_HEIGHT*3
            elif dir == DIRECTIONS.DOWN:
                end_y += TILE_HEIGHT*3
                start_y += TILE_HEIGHT
            elif dir == DIRECTIONS.RIGHT:
                end_x += TILE_WIDTH*3
                start_x += TILE_WIDTH
            elif dir == DIRECTIONS.LEFT:
                end_x -= TILE_WIDTH*3
            pygame.draw.line(self.screen, color, [start_x, start_y], [end_x, end_y], 3)

    def _check_shot(self, shot):
        start_x, start_y, color, dir, ind = shot.get_object()
        shot_info = "%d%d%d" % (ind, start_x, start_y)
        if shot_info in self.already_shot:
            end_x = start_x
            end_y = start_y
            self._check_hit(self.browns, dir, end_x, end_y, start_x, start_y, shot_info)
            self._check_hit(self.whites, dir, end_x, end_y, start_x, start_y, shot_info)

    def _check_hit(self, container, dir, end_x, end_y, start_x, start_y, shot_info):
        for person in container:
            if person:
                x, y = person.get_pos()
                person_info = "%d%d%d" % (person.ind, x, y)
                if shot_info != person_info:
                    is_hit = False
                    if dir == DIRECTIONS.RIGHT:
                        end_x += TILE_WIDTH
                        if x <= end_x and x >= start_x and y == start_y:
                            is_hit = True
                    elif dir == DIRECTIONS.LEFT:
                        end_x -= TILE_WIDTH
                        if x >= end_x and x <= start_x and y == start_y:
                            is_hit = True
                    elif dir == DIRECTIONS.UP:
                        end_y -= TILE_HEIGHT
                        if y >= end_y and y <= start_y and x == start_x:
                            is_hit = True
                    elif dir == DIRECTIONS.DOWN:
                        end_y += TILE_HEIGHT
                        if y <= end_y and y >= start_y and x == start_x:
                            is_hit = True
                    if is_hit:
                        ind = person.ind - 1
                        container[ind] = None

    def _check_alive(self, container):
        team_alive = True
        x = list(set(container))
        if len(x) == 1 and x[0] == None:
            team_alive = False
        return team_alive


if __name__ == "__main__":
    # Initialize the game engine
    pygame.init()
    h = TILE_HEIGHT * MAP_HEIGHT
    w = TILE_WIDTH * MAP_WIDTH
    Game([h, w]).main()