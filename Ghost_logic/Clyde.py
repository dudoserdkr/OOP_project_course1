from Ghost import Ghost


class Clyde(Ghost):
    def __init__(self):
        super().__init__()


    def _calc_target_coordinates(self, pacman_y, pacman_x):
        y, x = self.position
        if (pacman_y - y) ** 2 + (pacman_x - x) ** 2 <= 64:
            return pacman_y, pacman_x
        else:
            self.condition = 1
            
