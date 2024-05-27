import tkinter as tk
from PIL import Image, ImageTk
import os
from constants import CELL_SIZE
from Window import Window
from Canvas import CANVAS
from Ghost_logic.Blinky import Blinky
from FieldDrawing import FieldDrawing
from Field import FIELD
from random import randint
from Ghost_logic.Pinky import Pinky
from Ghost_logic.Inky import Inky
from Ghost_logic.Clyde import Clyde



class GhostDrawer:
    DELTA = 2
    def __init__(self, ghost):
        ghost_images = {
            Blinky: 'Blinky.png',
            Pinky: 'Pinky.png',
            Inky: 'Inky.png',
            Clyde: 'Clyde.png'
        }

        if type(ghost) in ghost_images:
            image_path = os.path.join(os.path.dirname(__file__), '..', 'pictures', ghost_images[type(ghost)])
            self.ghost_avatar = ImageTk.PhotoImage(
                Image.open(image_path).resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS))

        self.canvas = CANVAS
        self.ghost = ghost
        self.avatar_id = self.canvas.create_image(23, 13, anchor=tk.NW, image=self.ghost_avatar)
        self.position = self.multiple_coords_by_cell_size(self.ghost.position)
        self.moving_direction = None
        self.picture_name = self.ghost.__class__.__name__
        self.moving_phase = '1'
        self.ghost_avatar = None

    def draw(self):
        if self.ghost.next_move is None:
            self.ghost.move()

        curr_y, curr_x = self.position
        next_y, next_x = self.multiple_coords_by_cell_size(self.ghost.next_move)

        if self.ghost.position == (14, 1) or self.ghost.position == (14, 26):
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

        self.change_picture_in_move(direction=moving_direction)

        self.canvas.coords(self.avatar_id, curr_x, curr_y)

        Window.after(40, self.draw)

    def change_picture_in_move(self, direction) -> None:
        # TODO: УБРАТЬ ГАВНАКОД (Фікситься переіменуванням спрайтів Up в Down і навпаки, мені просто в лом.)
        if direction == 'Up':
            direction = 'Down'
        elif direction == 'Down':
            direction = 'Up'

        if self.moving_phase == '1':
            self.moving_phase = '2'
        else:
            self.moving_phase = '1'

        image_name = self.picture_name + direction + self.moving_phase + ".png"

        image_path = os.path.join(os.path.dirname(__file__), '..', 'pictures_ghost', image_name)
        self.ghost_avatar = ImageTk.PhotoImage(
            Image.open(image_path).resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS)
        )
        self.canvas.itemconfig(self.avatar_id, image=self.ghost_avatar)


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
    binky = Blinky()
    pinky = Pinky()
    inky = Inky()
    clyde = Clyde()
    # while True:
    #     y = randint(0, 30)
    #     x = randint(0, 27)
    #     if FIELD[y][x] == 0:
    #         break

    pinky.position = (14, 4)

    binky.condition = pinky.SPAWNING
    pinky.condition = pinky.SPAWNING
    inky.condition = inky.SPAWNING
    clyde.condition = clyde.SPAWNING
    drawer = GhostDrawer(pinky)
    drawer2 = GhostDrawer(binky)
    drawer3 = GhostDrawer(inky)
    drawer4 = GhostDrawer(clyde)
    pinky.move()
    print(pinky.walking_path)
    drawer.draw()
    drawer2.draw()
    drawer3.draw()
    drawer4.draw()
    Window.mainloop()
