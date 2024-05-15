from Ghost import Ghost
from Field import FIELD_WIDTH, FIELD_HEIGHT


class Pinky(Ghost):
    def __init__(self):
        super().__init__()

    def _calc_targer_coordinates(self, pacman_y: int, pacman_x: int, pacman_direction: str) -> tuple:

        dy, dx = self._define_deltas(pacman_direction)

        target_y, target_x = pacman_y + dy * 4, pacman_x + dx * 4

        if self.check_coordinates_validity(target_y, target_x):
            if self.field[target_y][target_x] == 0:
                return target_y, target_x

            else:
                for i in range(1, FIELD_HEIGHT):
                    target_y, target_x = pacman_y + dy * (4 + i), pacman_x + dx * (4 + i)
                    if self.check_coordinates_validity(target_y, target_x):
                        if self.field[target_y][target_x] == 0:
                            return target_y, target_x
                    else:
                        break

        return pacman_y, pacman_x

    def _find_way_to_pacman(self, pacman_y: int, pacman_x: int, pacman_direction=None):
        pacman_y, pacman_x = self._calc_targer_coordinates(pacman_y, pacman_x, pacman_direction)

        super()._find_way_to_pacman(pacman_y, pacman_x)

