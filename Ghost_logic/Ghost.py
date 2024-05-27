from Field import FIELD, FIELD_WIDTH, FIELD_HEIGHT
from copy import deepcopy
from random import randint
from abc import ABCMeta, abstractmethod

class Ghost(metaclass=ABCMeta):
    START_POSITION = (11, 14)
    SCARED = 0
    WALKING = 1
    HUNTING = 2

    def __init__(self) -> None:
        """
        self.position: tuple, (y, x) - current coordinates of the ghost on the FIELD

        self.condition: int, self.condition influences on ghost behavior,
            If self.condition == 0. Ghost starting to move in a random way.
            If self.condition == 1. Ghost just walking to a random cell, which must be far away from pacman
            If self.condition == 2. Ghost trying to catch pacman, using his own stategy

        self.way_to_pacman: list of tuples (y, x) - current shorter way to pacman given by bfs alg
        """
        self.field = FIELD
        self.position = self.START_POSITION
        self.next_move = None
        self.target_coords = None

        self.blinky = None
        self.pacman = None
        self.pacman_last_position = None

        self.walking_path = []
        self.way_to_pacman = []
        self.condition = 1



    def set_pacman(self, pacman):
        self.pacman = pacman

    def set_blinky(self, blinky):
        self.blinky = blinky

    def get_blinky_poistion(self):
        if self.blinky is not None:
            return self.blinky.position


    # region walking
    @abstractmethod
    def get_walking_path(self):
        pass

    @abstractmethod
    def get_walking_start_coordinates(self):
        pass

    # endregion


    def move(self) -> None:
        if self.condition == Ghost.SCARED:
            self.random_move()

        elif self.condition == Ghost.WALKING: # TODO: Перевірити, чи не зламались інші привиди
            if self.walking_path:
                (possible_y, possible_x) = self.walking_path.pop(0)
                curr_y, curr_x = self.position

                if abs((curr_y + curr_x) - (possible_y + possible_x)) != 1:
                    walking_path = self.get_walking_path()

                    if self.position in walking_path:
                        index = walking_path.index(self.position)

                        if index == len(walking_path) - 1:
                            return self.move()

                        else:
                            self.next_move = walking_path[index + 1]

                    else:
                        return self.move()
                else:
                    self.next_move = (possible_y, possible_x)



            else:
                y, x = self.get_walking_start_coordinates()
                path_to_walking_cell = self.path_to_trgt(y, x)
                self.walking_path = path_to_walking_cell + self.get_walking_path()
                self.next_move = self.walking_path.pop(0)

        elif self.condition == Ghost.HUNTING:  # TODO: розібратись з пакмен дірекшен
            try:
                if self.pacman_last_position != self.pacman.position:
                    self.build_way_to_target(self.pacman.position, self.pacman.direction, self.get_blinky_poistion())
                    self.next_move = self.way_to_pacman.pop(0)
                    self.pacman_last_position = deepcopy(self.pacman.position)

                elif self.pacman_last_position == self.pacman.position:
                        self.next_move = self.way_to_pacman.pop(0)
            except IndexError:
                self.next_move = deepcopy(self.position)

    # region Scared

    def random_move(self) -> None:
        curr_y, curr_x = self.position
        possible_moves = list(self._ghost_possible_moves(curr_y, curr_x))
        random_number = randint(0, len(possible_moves) - 1)
        self.next_move = possible_moves[random_number]

    # endregion

    # In this region there are methods, needed to finding the shortet way to the pacman
    # region Hunting

    def build_way_to_target(self, pacman_position: tuple, pacman_direction=None, blinky_position=None) -> None:
        pacman_y, pacman_x = pacman_position
        self.way_to_pacman = self.path_to_trgt(pacman_y, pacman_x)

    def path_to_trgt(self, y, x) -> list[list]:
        tempory_board = self._find_way_to_pacman(y, x)
        if tempory_board is None:
            raise ValueError("Координати, які були передані в функцію path_to_trgt є некоректними.")
        return self._rebuild_path(tempory_board, y, x)

    def _ghost_possible_moves(self, y: int, x: int):
        """
        yielding every possible coordinates where ghost can move by 1 step
        """
        # deltas = [
        #     (i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 and j != 0
        # ]

        deltas = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]

        for dy, dx in deltas:
            new_y, new_x = y + dy, x + dx

            if self.check_coordinates_validity(new_y, new_x):
                if self.field[new_y][new_x] == 0 or self.field[new_y][new_x] == 2:
                    yield new_y, new_x
                elif self.field[new_y][new_x] == 3: # TODO: зробити можливість проходити через бар'єри
                    if new_y == 27:
                        yield 14, 1
                    else:
                        yield 14, 26

    def _find_way_to_pacman(self, pacman_y: int, pacman_x: int):
        """Finding the most shorter way to reach pacman by using bfs alg"""

        curr_y, curr_x = self.position

        tempory_board = deepcopy(self.field)
        visited_board = [
            [None for _ in range(FIELD_WIDTH)]
            for _ in range(FIELD_HEIGHT)
        ]
        pass
        tempory_board[curr_y][curr_x] = self.position
        visited_board[curr_y][curr_x] = 1

        queue = [
            ((new_y, new_x), 0, (curr_y, curr_x))
            for new_y, new_x in self._ghost_possible_moves(curr_y, curr_x)
        ]

        while queue:
            (curr_y, curr_x), moves_amount, from_where = queue.pop(0)

            if curr_y == pacman_y and curr_x == pacman_x:
                tempory_board[curr_y][curr_x] = from_where
                return tempory_board

            if visited_board[curr_y][curr_x] is not None:
                continue

            tempory_board[curr_y][curr_x] = from_where
            visited_board[curr_y][curr_x] = 1

            queue += [
                ((new_y, new_x), moves_amount + 1, (curr_y, curr_x))
                for new_y, new_x in self._ghost_possible_moves(curr_y, curr_x)
            ]

    def _rebuild_path(self, tempory_board: list[list], pacman_y: int, pacman_x: int) -> list:
        """
        :param tempory_board: deepcopy of self.field, but in cell instead of 0 it contains tuple (y, x),
                                                          (y, x) -- coordinates of the cell we came from

        :return: list of coordinates, where rebuilded_path[0] == start ghost position, and
        rebuilded_path[len(rebuilded_path) - 1] == (pacman_y, pacman_x)
        """

        rebuilded_path = []

        current_position = (pacman_y, pacman_x)

        while current_position != self.position:
            rebuilded_path.append(current_position)
            x, y = current_position
            current_position = tempory_board[x][y]

        pass

        """
        після циклу ми отримали повний шлях (список з кортежів, де кортежі вигляду (y, x)). Нам треба його перевенути
        щоб перша координати стала останньою, а остання першою. Також треба виключити у вже перевернутом списку першу координату.
        Бо перша координата - поточне положення привида, яке і так міститься в self.position
        """
        return rebuilded_path[::-1]
    # endregion

    @staticmethod
    def check_coordinates_validity(y, x):
        return 0 <= y <= FIELD_HEIGHT - 1 and 0 <= x <= FIELD_WIDTH - 1

    @staticmethod
    def define_deltas(moving_direction: str) -> tuple:
        dx = dy = 0

        if moving_direction == 'Up':
            dy, dx = 1, 0
        elif moving_direction == 'Down':
            dy, dx = -1, 0
        elif moving_direction == 'Right':
            dy, dx = 0, 1
        elif moving_direction == 'Left':
            dy, dx = 0, -1

        return dy, dx

    def find_nearest_free_cell(self, y: int, x: int):
        deltas = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]

        visited_board = deepcopy(self.field)

        queue = [(y, x)]

        while queue:
            curr_y, curr_x = queue.pop(0)

            for dy, dx in deltas:
                ny, nx = curr_y + dy, curr_x + dx
                if self.check_coordinates_validity(ny, nx):
                    if visited_board[ny][nx] is not None:
                        if self.field[ny][nx] == 0:
                            return ny, nx
                        else:
                            queue.append((ny, nx))
                            visited_board[ny][nx] = None




if __name__ == '__main__':
    ghost = Ghost()
    ghost.build_way_to_target(23, 15)
    ghost.random_move()
    print(ghost.field[23][15])
    print(ghost.find_nearest_free_cell(0, 11))
    print(ghost.next_move)

    print(ghost.way_to_pacman)
    # print(temp_field)
    #
    # for i in temp_field:
    #     for j in i:
    #         print(j, end='\t\t\t\t\t')
    #     print()
