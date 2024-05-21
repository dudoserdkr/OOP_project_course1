from Ghost import Ghost


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
                target_y, target_x = self.find_nearest_free_cell(target_y, target_x)
                return target_y, target_x
        else:
            return pacman_y, pacman_x


    def build_way_to_pacman(self, pacman_y, pacman_x, pacman_direction=None) -> None:
        pacman_y, pacman_x = self._calc_targer_coordinates(pacman_y, pacman_x, pacman_direction)
        super().build_way_to_pacman(pacman_y, pacman_x, pacman_direction)



if __name__ == '__main__':
    p = Pinky()
    print(p.build_way_to_pacman(23, 11, 'Right'))
    print(p.way_to_pacman)


