from tkinter import *
from PIL import ImageTk, Image

from PacMan import PacMan
from FieldDrawing import FieldDrawing
from constants import CELL_SIZE, DELAY
from Window import Window


class VisualPacMan(PacMan):
    def __init__(self):
        PacMan.__init__(self)
        self.canvas_position = [13 * CELL_SIZE, 23*CELL_SIZE]
        self.left_pacman = Image.open("pictures/PacMan_left.png")
        self.

    def create_pacman(self):
        image = self.left_pacman  # TODO: change image
        resized_image = image.resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS)
        pacman_photo = ImageTk.PhotoImage(resized_image)
        return .create_image(pacman_canvas_position[0] + 10, pacman_canvas_position[1] + 10, image=pacman_photo)
