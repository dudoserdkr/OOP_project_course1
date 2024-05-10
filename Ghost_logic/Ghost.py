from Field import FIELD, FIELD_WIDTH, FIELD_HEIGHT
from copy import deepcopy


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

        self.way_to_pacman = []
        self.condition = 1

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

            if 0 <= new_y <= FIELD_WIDTH and 0 <= new_x <= FIELD_HEIGHT:
                if self.field[new_y][new_x] == 0 or self.field[new_y][new_x] == 2:
                    yield new_y, new_x

    def _find_way_to_pacman(self, pacman_y: int, pacman_x: int) -> None or list[list]:
        """Finding the most shorter way to reach pacman by using bfs alg"""

        curr_y, curr_x = self.position

        tempory_board = deepcopy(self.field)
        visited_board = [
            [None for _ in range(FIELD_WIDTH)]
            for _ in range(FIELD_HEIGHT)
        ]

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

    def build_way_to_pacman(self, pacman_y, pacman_x) -> None:
        tempory_board = self._find_way_to_pacman(pacman_y, pacman_x)
        self.way_to_pacman = self._rebuild_path(tempory_board, pacman_y, pacman_x)


if __name__ == '__main__':
    ghost = Ghost()
    ghost.build_way_to_pacman(23, 11)

    print(ghost.way_to_pacman)
    # print(temp_field)
    #
    # for i in temp_field:
    #     for j in i:
    #         print(j, end='\t\t\t\t\t')
    #     print()
