from tkinter import *
from PIL import ImageTk, Image

from PacMan import PacMan
from Ghost import Ghost
from FieldDrawing import FieldDrawing

from Window import Window
from Field import FIELD
from constants import CELL_SIZE, DELAY
from Canvas import CANVAS

class VisualGhost(Ghost):
    def __init__(self):
        super().__init__()
        # self.absolut_speed = DELAY / self.speed
        self.canvas_position = [self.position[0] * CELL_SIZE, self.position[0] * CELL_SIZE]
        self.left_pacman = Image.open("pictures/PacMan_left.png")
        self.canvas = CANVAS
        self.pacman_photo = None
        self.id = self.create_pacman()

        self.is_moving = False
        self.current_move_proces = None
        self.moving_proces_id = None


