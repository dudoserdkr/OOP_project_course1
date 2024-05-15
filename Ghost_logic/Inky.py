from Ghost import Ghost

class Inky(Ghost):
    def __init__(self):
        super().__init__()

    def _calc_target_coordinates(self, pacman_y: int, pacman_x: int, blinky_y: int, blinky_x: int, direction: str) -> tuple:
        dy, dx = self._define_deltas(direction)

        # calculating pacman coordinates + 2 to one of the corrdinates with respect to direction
        # for example: if pacman looking to the right:
        # pacman_y = pacman_y, pacman_x = 2 + pacman_x
        pacman_y, pacman_x = pacman_y + 2 * dy, pacman_x + 2 * dx

        target_y, target_x = 2 * (pacman_y - blinky_y) + blinky_y, 2 * (pacman_x - blinky_x) + blinky_x

        return target_y, target_x

    def build_way_to_pacman(self, pacman_y, pacman_x, blinky_y, blinky_x, pacman_direction=None) -> None:

        target_y, target_x = self._calc_target_coordinates(pacman_y, pacman_x,
                                                           blinky_y, blinky_x,
                                                           pacman_direction)
        super().build_way_to_pacman(target_y, target_x, pacman_direction)