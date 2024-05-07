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
        self.canvas_position = [13 * CELL_SIZE, 23 * CELL_SIZE]
        self.left_pacman = Image.open("pictures/PacMan_left.png")
        self.canvas = CANVAS
        self.pacman_photo = None
        self.id = self.create_pacman()

    def create_pacman(self):
        image = self.left_pacman  # TODO: change picture
        resized_image = image.resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS)
        self.pacman_photo = ImageTk.PhotoImage(resized_image)
        id = self.canvas.create_image(self.canvas_position[0] + 10, self.canvas_position[1] + 10, image=self.pacman_photo)

        return id

    def move_up(self, event):
        if self.can_move_up():
            self.canvas.move(self.id, 0, -CELL_SIZE)
            self.position[0] -= 1
            Window.after(DELAY, lambda: self.move_up(event))
        return

    def move_down(self, event):
        if self.can_move_down():
            self.canvas.move(self.id, 0, CELL_SIZE)
            self.position[0] += 1
            Window.after(DELAY, lambda: self.move_down(event))
        return

    def move_right(self, event):
        if self.can_move_right():
            self.canvas.move(self.id, CELL_SIZE, 0)
            self.position[1] += 1
            Window.after(DELAY, lambda: self.move_right(event))
        return

    def move_left(self, event):
        if self.can_move_left():
            self.canvas.move(self.id, -CELL_SIZE, 0)
            self.position[1] -= 1
            Window.after(DELAY, lambda: self.move_left(event))  # TODO: DELAY * self.speed
        return

if __name__ == "__main__":
    m = FieldDrawing(FIELD)
    m.draw_field()
    vp = VisualPacMan()
    Window.bind('<Left>', vp.move_left)
    Window.bind('<Right>', vp.move_right)
    Window.bind('<Up>', vp.move_up)
    Window.bind('<Down>', vp.move_down)
    Window.mainloop()