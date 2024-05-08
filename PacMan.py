from Field import FIELD, PACMAN_START_POS


class PacMan:

    START_POS = PACMAN_START_POS

    PACMAN_ALIVE = True
    PACMAN_DEAD = False

    def __init__(self) -> None:
        self.position = self.START_POS

        self.life_status = self.PACMAN_ALIVE

        self.speed = 1  # influencing on how fast pacman image will be refreshing
        self.field = FIELD

        # self.availible_lifes = 3  Work in Progress for pacman alive status

    def check_field_cell(self, dy: int, dx: int) -> bool:
        curr_y, curr_x = self.position
        return not (self.field[curr_y + dy][curr_x + dx] == 1 or self.field[curr_y + dy][curr_x + dx] == 2)

    # region move_allowers functions

    def can_move_left(self) -> bool:
        dy, dx = 0, -1
        return self.check_field_cell(dy, dx)

    def can_move_right(self) -> bool:
        dy, dx = 0, 1
        return self.check_field_cell(dy, dx)

    def can_move_up(self) -> bool:
        dy, dx = -1, 0
        return self.check_field_cell(dy, dx)

    def can_move_down(self) -> bool:
        dy, dx = 1, 0
        return self.check_field_cell(dy, dx)

    # endregion

    # def death(self):
    #     self.condition = False  # Means he is dead
    #     self.position = self.START_POS
