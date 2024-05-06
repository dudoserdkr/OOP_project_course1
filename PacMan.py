from Object import Object


class PacMan(Object):

    START_POS = (13, 23)
    PACMAN_DEAD = False
    PACMAN_ALIVE = True

    def __init__(self):
        self.position = self.START_POS
        self.condition = self.PACMAN_ALIVE
        self.speed = 1

    def move(self, dx, dy):
        curr_x, curr_y = self.position

        self.position = curr_x + dx, curr_y + dy

    def death(self):
        self.condition = self.PACMAN_DEAD
        self.position = self.START_POS
