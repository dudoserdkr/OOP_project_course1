from Ghost_logic.Ghost import Ghost


class Blinky(Ghost):
    def __init__(self):
        super().__init__()

    pass

    def get_walking_path(self) -> list:
        return [
            (5, 22), (5, 23), (5, 24), (5, 25), (5, 26),
            (4, 26), (3, 26), (2, 26), (1, 26), (1, 25), (1, 24), (1, 23),
            (1, 22), (1, 21), (2, 21), (3, 21), (4, 21)
        ]

    def get_walking_start_coordinates(self) -> tuple:
        return 5, 21

if __name__ == '__main__':
    ghost = Blinky()
    ghost.position = (29, 6)
    ghost.condition = ghost.WALKING
    ghost.move()