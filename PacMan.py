from Field import Field

class PacMan:

    START_POS = (13, 23)
    PACMAN_CURRENT_STATUS = True  # current life True/False
    AVAILABLE_LIVES = 3

    def __init__(self):
        self.position = self.START_POS

        self.condition = self.PACMAN_CURRENT_STATUS

        self.speed = 1

        self.field = Field().map

    def move(self, dx, dy):
        curr_x, curr_y = self.position

        self.position = curr_x + dx, curr_y + dy

    def death(self):
        self.condition = False  # Means he is dead
        self.position = self.START_POS
