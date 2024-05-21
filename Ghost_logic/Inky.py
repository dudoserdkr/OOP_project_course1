from Ghost import Ghost


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

    def _calc_target_coordinates(self, pacman_y: int, pacman_x: int, blinky_y: int, blinky_x: int, direction: str) -> tuple:
        dy, dx = self._define_deltas(direction)

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

    def build_way_to_pacman(self, pacman_y, pacman_x, blinky_y, blinky_x, pacman_direction=None) -> None:

        target_y, target_x = self._calc_target_coordinates(pacman_y, pacman_x,
                                                           blinky_y, blinky_x,
                                                           pacman_direction)
        super().build_way_to_pacman(target_y, target_x, pacman_direction)


if __name__ == '__main__':
    p = Inky()
    print(p.build_way_to_pacman(23, 11,
                                16, 14,
                                'Right'))
    print(p.way_to_pacman)

