from Ghost_logic.Ghost import Ghost


class Clyde(Ghost):
    def __init__(self):
        super().__init__()

    def get_walking_path(self):
        return [
            (24, 6), (25, 6), (26, 6), (26, 5), (26, 4), (26, 3), (26, 2), (26, 1), (27, 1),
            (28, 1), (29, 1), (29, 2), (29, 3), (29, 4), (29, 5), (29, 6), (29, 7), (29, 8),
            (29, 9), (29, 10), (29, 11), (29, 12), (28, 12), (27, 12), (26, 12), (26, 11),
            (26, 10), (26, 9), (25, 9), (24, 9), (23, 9), (23, 7)
                ]

    def get_walking_start_coordinates(self):
        return 23, 6

    def _calc_target_coordinates(self, pacman_position):
        pacman_y, pacman_x = pacman_position
        y, x = self.position
        if (pacman_y - y) ** 2 + (pacman_x - x) ** 2 <= 64:
            return pacman_y, pacman_x
        else:
            return self.get_walking_start_coordinates()

    def build_way_to_target(self, pacman_position: tuple, pacman_direction=None, blinky_position=None) -> None:

        target_coordinates = self._calc_target_coordinates(pacman_position)

        super().build_way_to_target(target_coordinates)


            
if __name__ == '__main__':
    c = Clyde()
    print(c.get_walking_path())