from Field import FIELD


class PacMan:

    START_POS = [23, 13]
    PACMAN_CURRENT_STATUS = True  # current life True/False

    def __init__(self):
        self.position = self.START_POS.copy()

        self.condition = self.PACMAN_CURRENT_STATUS

        self.speed = 1

        self.field = FIELD

        self.available_lives = 3

    def can_move_left(self):
        curr_y, curr_x = self.position
        if self.field[curr_y][curr_x - 1] == 1 or self.field[curr_y][curr_x - 1] == 2:
            return False
        self.position[1] -= 1
        return True

    def can_move_right(self):
        curr_y, curr_x = self.position
        if self.field[curr_y][curr_x + 1] == 1 or self.field[curr_y][curr_x + 1] == 2:
            return False
        self.position[1] += 1
        return True

    def can_move_up(self):
        curr_y, curr_x = self.position
        if self.field[curr_y - 1][curr_x] == 1 or self.field[curr_y - 1][curr_x] == 2:
            return False
        self.position[0] -= 1
        return True

    def can_move_down(self):
        curr_y, curr_x = self.position
        if self.field[curr_y + 1][curr_x] == 1 or self.field[curr_y + 1][curr_x] == 2:
            return False
        self.position[0] += 1
        return True

    def death(self):
        self.condition = False  # Means he is dead
        self.position = PacMan.START_POS