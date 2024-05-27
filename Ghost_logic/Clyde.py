from Ghost_logic.Ghost import Ghost
from copy import deepcopy


class Clyde(Ghost):
    START_POSITION = (15, 11)
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

    def check_distance_to_pacman(self, pacman_position) -> bool :
        """
        if clyde distance to pacman <= 8 returns True
        else returns False
        """

        pacman_y, pacman_x = pacman_position
        y, x = self.position

        distance_squared = (pacman_y - y) ** 2 + (pacman_x - x) ** 2
        radius_squared = 64

        if distance_squared <= radius_squared:
            return True
        else:
            return None

    def move(self) -> None:
        if self.check_distance_to_pacman(self.pacman.position) and self.condition == Ghost.HUNTING:
            self.condition = Ghost.WALKING
            super().move()
            self.condition = Ghost.HUNTING
        else:
            super().move()



            
if __name__ == '__main__':
    c = Clyde()
    print(c.get_walking_path())