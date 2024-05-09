from tkinter import *
from PIL import ImageTk, Image

from PacMan import PacMan
from FieldDrawing import FieldDrawing

from Window import Window
from Field import FIELD
from constants import CELL_SIZE, DELAY
from Canvas import CANVAS


class VisualPacMan(PacMan):
    def __init__(self):
        super().__init__()
        # self.absolut_speed = DELAY / self.speed
        self.canvas_position = [13 * CELL_SIZE, 23 * CELL_SIZE]
        self.left_pacman = Image.open("pictures/PacMan_left.png")
        self.canvas = CANVAS
        self.pacman_photo = None
        self.id = self.create_pacman()

        self.is_moving = False
        self.current_move_proces = None
        self.moving_proces_id = None

    def create_pacman(self):
        image = self.left_pacman  # TODO: change picture
        resized_image = image.resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS)
        self.pacman_photo = ImageTk.PhotoImage(resized_image)
        id = self.canvas.create_image(self.canvas_position[0] + 10, self.canvas_position[1] + 10, image=self.pacman_photo)

        return id

    def move_up(self, event,  skip_first_if=False):
        if self.is_moving and self.current_move_proces == "up" and not skip_first_if:
            return
        if self.can_move_up():
            self.stop_moving()
            self.is_moving = True
            self.current_move_proces = "up"

            self.canvas.move(self.id, 0, -CELL_SIZE)
            self.position[0] -= 1
            self.moving_proces_id = Window.after(DELAY, lambda: self.move_up(event, True))

        return

    def move_down(self, event, skip_first_if=False):
        if self.is_moving and self.current_move_proces == "down" and not skip_first_if:
            return
        if self.can_move_down():
            self.stop_moving()
            self.is_moving = True
            self.current_move_proces = "down"

            self.canvas.move(self.id, 0, CELL_SIZE)
            self.position[0] += 1
            self.moving_proces_id = Window.after(DELAY, lambda: self.move_down(event, True))
        return

    def move_right(self, event, skip_first_if=False):
        if self.is_moving and self.current_move_proces == "right" and not skip_first_if:
            return
        if self.can_move_right():
            self.stop_moving()
            self.is_moving = True
            self.current_move_proces = "right"

            self.canvas.move(self.id, CELL_SIZE, 0)
            self.position[1] += 1
            self.moving_proces_id = Window.after(DELAY, lambda: self.move_right(event, True))
        return

    def move_left(self, event, skip_first_if=False):
        if self.is_moving and self.current_move_proces == "left" and not skip_first_if:
            return
        if self.can_move_left():
            self.stop_moving()
            self.is_moving = True
            self.current_move_proces = "left"

            self.canvas.move(self.id, -CELL_SIZE, 0)
            self.position[1] -= 1
            self.moving_proces_id = Window.after(DELAY, lambda: self.move_left(event, True))  # TODO: DELAY / self.speed
        return

    def stop_moving(self):
        self.is_moving = False
        self.current_move_proces = None
        if self.moving_proces_id is not None:
            self.canvas.after_cancel(self.moving_proces_id)
git 
if __name__ == "__main__":
    m = FieldDrawing(FIELD)
    m.draw_field()
    vp = VisualPacMan()
    Window.bind('<Left>', vp.move_left)
    Window.bind('<Right>', vp.move_right)
    Window.bind('<Up>', vp.move_up)
    Window.bind('<Down>', vp.move_down)
    Window.mainloop()