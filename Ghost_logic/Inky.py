from Ghost_logic.Ghost import Ghost


"""
Інкі працює наступним чином:
функція _calc_target_coordinates бере координати пакмана, враховуючи напрямок його руху, додає +2 або -2 до його поточних координат, назвемо ці координати - новими координатами пакмена;
далі бере координати блінкі, і робить обрахунок: target_y, target_x = 2 * (pacman_y - blinky_y) + blinky_y, 2 * (pacman_x - blinky_x) + blinky_x; pacman_y, pacman_x - нові координати пакмена.
Якщо ці координати виходять за межі дошки - повертається позиція блінкі
Якщо на цих координатах знаходиться бар'єр - шукаємо по бфс найближчу вільну клітину
Якщо точка на мапі, якій відповідають ці координати є вільною - поветраємо координати 
"""


class Inky(Ghost):
    def __init__(self):
        super().__init__()

    def get_walking_path(self):
           return [
             (23, 19), (23, 20), (23, 21), (24, 21), (25, 21), (26, 21), (26, 22), (26, 23), (26, 24), (26, 25), (26, 26), (27, 26),
             (28, 26), (29, 26), (29, 25), (29, 24), (29, 23), (29, 22), (29, 21), (29, 20), (29, 19), (29, 18), (29, 17), (29, 16),
             (29, 15), (28, 15), (27, 15), (26, 15), (26, 16), (26, 17), (26, 18), (25, 18), (24, 18)
           ]

    def get_walking_start_coordinates(self):
        return 23, 18

    def _calc_target_coordinates(self, pacman_y: int, pacman_x: int, direction: str, blinky_y: int, blinky_x: int) -> tuple:
        dy, dx = self.define_deltas(direction)

        # calculating pacman coordinates + 2 to one of the corrdinates with respect to direction
        # for example: if pacman looking to the right:
        # pacman_y = pacman_y, pacman_x = 2 + pacman_x
        pacman_y, pacman_x = pacman_y + 2 * dy, pacman_x + 2 * dx

        target_y, target_x = 2 * (pacman_y - blinky_y) + blinky_y, 2 * (pacman_x - blinky_x) + blinky_x
        if self.check_coordinates_validity(target_y, target_x):
            if self.field[target_y][target_x] == 0:
                return target_y, target_x
            else:
                target_y, target_x = self.find_nearest_free_cell(target_y, target_x)
                return target_y, target_x
        else:
            return blinky_y, blinky_x

    def build_way_to_target(self, pacman_position, pacman_direction=None, blinky_position=None) -> None:

        pacman_y, pacman_x = pacman_position
        blinky_y, blinky_x = blinky_position

        target_coordinates = self._calc_target_coordinates(
                                                           pacman_y, pacman_x,
                                                           pacman_direction,
                                                           blinky_y, blinky_x,
                                                           )
        super().build_way_to_target(target_coordinates)


if __name__ == '__main__':
    p = Inky()
    print(p.get_walking_path())
