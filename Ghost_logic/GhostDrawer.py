import tkinter as tk
from PIL import Image, ImageTk
import os
from constants import CELL_SIZE
from Window import Window
from Canvas import CANVAS
from Blinky import Blinky


class GhostDrawer:
    DELTA = CELL_SIZE / 5
    def __init__(self, ghost):
        self.ghost_avatar = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), '..', 'pictures', 'Blinky.png')).resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS))
        self.canvas = CANVAS
        self.ghost = ghost
        self.avatar_id = self.canvas.create_image(23, 13, anchor=tk.NW, image=self.ghost_avatar)
        self.position = self.multiple_coords_by_cell_size(self.ghost.position)
        self.moving_direction = None

    def draw(self):
        curr_y, curr_x = self.position
        next_y, next_x = self.multiple_coords_by_cell_size(self.ghost.next_move)

        if (curr_y, curr_x) == (next_y, next_x):
            pass

        moving_direction = self.define_direction(self.position, (next_y, next_x))
        dy, dx = self.ghost.define_deltas(moving_direction)
        self.moving_direction = moving_direction

        curr_y += self.DELTA * dy
        curr_x += self.DELTA * dx
        self.position = curr_y, curr_x

        self.canvas.coords(self.avatar_id, curr_y, curr_x)
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
            self.moving_direction = "Left"
        elif curr_y == next_y and curr_x < next_x:
            self.moving_direction = "Right"
        elif curr_x == next_x and curr_y > next_y:
            self.moving_direction = "Down"
        else:
            self.moving_direction = "Up"


if __name__ == '__main__':
    ghost = Blinky()
    ghost.next_move = (11, 20)
    drawer = GhostDrawer(ghost)
    drawer.draw()
