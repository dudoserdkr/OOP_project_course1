from Ghost_logic.Ghost import Ghost


class Pinky(Ghost):
    def __init__(self):
        super().__init__()

    def get_walking_path(self):
        return [
            (4, 6), (3, 6), (2, 6), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1),
            (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)
                ]

    def get_walking_start_coordinates(self):
        return 5, 6

    def _calc_targer_coordinates(self, pacman_y: int, pacman_x: int, pacman_direction: str) -> tuple:

        dy, dx = self.define_deltas(pacman_direction)

        target_y, target_x = pacman_y + dy * 4, pacman_x + dx * 4

        if self.check_coordinates_validity(target_y, target_x):
            if self.field[target_y][target_x] == 0:
                return target_y, target_x

            else:
                target_y, target_x = self.find_nearest_free_cell(target_y, target_x)
                return target_y, target_x
        else:
            return pacman_y, pacman_x


    def build_way_to_target(self, pacman_position, pacman_direction=None, blinky_position=None) -> None:
        pacman_y, pacman_x = pacman_position
        target_coordinates = self._calc_targer_coordinates(pacman_y, pacman_x, pacman_direction)
        super().build_way_to_target(target_coordinates)



if __name__ == '__main__':
    p = Pinky()
    print(p.build_way_to_target(23, 11, 'Right'))
    print(p.way_to_pacman)


