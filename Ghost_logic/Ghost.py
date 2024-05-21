from Field import FIELD, FIELD_WIDTH, FIELD_HEIGHT
from copy import deepcopy
from random import randint


class Ghost:
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

        self.way_to_pacman = []
        self.condition = 1


    # region walking

    def walking(self):
        pass

    # endregion


    # region Scared

    def random_move(self) -> None:
        curr_y, curr_x = self.position
        possible_moves = list(self._ghost_possible_moves(curr_y, curr_x))
        random_number = randint(0, len(possible_moves) - 1)
        self.next_move = possible_moves[random_number]

    # endregion

    # In this region there are methods, needed to finding the shortet way to the pacman
    # region Hunting

    def build_way_to_pacman(self, pacman_y, pacman_x, pacman_direction=None) -> None:
        tempory_board = self._find_way_to_pacman(pacman_y, pacman_x)
        print(tempory_board[pacman_y][pacman_x])
        self.way_to_pacman = self._rebuild_path(tempory_board, pacman_y, pacman_x)
        self.next_move = self.way_to_pacman.pop(0)

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

    def _find_way_to_pacman(self, pacman_y: int, pacman_x: int):
        """Finding the most shorter way to reach pacman by using bfs alg"""

        curr_y, curr_x = self.position

        tempory_board = deepcopy(self.field)
        visited_board = [
            [None for _ in range(FIELD_WIDTH)]
            for _ in range(FIELD_HEIGHT)
        ]
        pass
        tempory_board[curr_y][curr_x] = None
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

    @staticmethod
    def _rebuild_path(tempory_board: list[list], pacman_y: int, pacman_x: int) -> list:
        """
        :param tempory_board: deepcopy of self.field, but in cell instead of 0 it contains tuple (y, x),
                                                          (y, x) -- coordinates of the cell we came from

        :return: list of coordinates, where rebuilded_path[0] == start ghost position, and
        rebuilded_path[len(rebuilded_path) - 1] == (pacman_y, pacman_x)
        """

        rebuilded_path = []

        current_position = (pacman_y, pacman_x)

        while current_position is not None:
            rebuilded_path.append(current_position)
            x, y = current_position
            current_position = tempory_board[x][y]

        return rebuilded_path[::-1]
    # endregion

    @staticmethod
    def check_coordinates_validity(y, x):
        return 0 <= y <= FIELD_WIDTH and 0 <= x <= FIELD_HEIGHT

    @staticmethod
    def _define_deltas(pacman_direction: str) -> tuple:
        dx = dy = 0

        if pacman_direction == 'Up':
            dy, dx = 1, 0
        elif pacman_direction == 'Down':
            dy, dx = -1, 0
        elif pacman_direction == 'Right':
            dy, dx = 0, 1
        elif pacman_direction == 'Left':
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
    ghost.build_way_to_pacman(23, 15)
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
