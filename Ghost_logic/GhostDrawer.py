import tkinter as tk
from PIL import Image, ImageTk
import os
from constants import CELL_SIZE
from Window import Window
from Canvas import CANVAS
from Blinky import Blinky
from FieldDrawing import FieldDrawing
from Field import FIELD
from random import randint


class GhostDrawer:
    DELTA = 2
    def __init__(self, ghost):
        self.ghost_avatar = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), '..', 'pictures', 'Blinky.png')).resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS))
        self.canvas = CANVAS
        self.ghost = ghost
        self.avatar_id = self.canvas.create_image(23, 13, anchor=tk.NW, image=self.ghost_avatar)
        self.position = self.multiple_coords_by_cell_size(self.ghost.position)
        self.moving_direction = None

    def draw(self):
        if self.ghost.next_move is None:
            self.ghost.move()

        curr_y, curr_x = self.position
        next_y, next_x = self.multiple_coords_by_cell_size(self.ghost.next_move)

        if self.ghost.position == (14, 1):
            self.position = next_y, next_x
            curr_y, curr_x = self.position

        if (curr_y, curr_x) == (next_y, next_x):
            self.ghost.position = self.ghost.next_move
            self.ghost.move()
            next_y, next_x = self.multiple_coords_by_cell_size(self.ghost.next_move)

        moving_direction = self.define_direction(self.position, (next_y, next_x))
        dy, dx = self.ghost.define_deltas(moving_direction)
        self.moving_direction = moving_direction


        curr_y += self.DELTA * dy
        curr_x += self.DELTA * dx
        self.position = curr_y, curr_x

        self.canvas.coords(self.avatar_id, curr_x, curr_y)
        Window.after(20, self.draw)

    @staticmethod
    def multiple_coords_by_cell_size(coords: tuple) -> tuple:
        y, x = coords
        y, x = y * CELL_SIZE, x * CELL_SIZE
        return y, x

    def define_direction(self, current_coord: tuple, next_coords: tuple) -> str:
        curr_y, curr_x = current_coord
        next_y, next_x = next_coords

        if curr_y == next_y and curr_x > next_x:
            return "Left"
        elif curr_y == next_y and curr_x < next_x:
            return "Right"
        elif curr_x == next_x and curr_y > next_y:
            return "Down"
        else:
            return "Up"


if __name__ == '__main__':
    field = FieldDrawing(FIELD)
    field.draw_field()
    ghost = Blinky()
    while True:
        y = randint(0, 30)
        x = randint(0, 27)
        if FIELD[y][x] == 0:
            break

    ghost.position = (14, 4)
    ghost.condition = ghost.WALKING
    drawer = GhostDrawer(ghost)
    ghost.move()
    print(ghost.walking_path)
    drawer.draw()
    Window.mainloop()
