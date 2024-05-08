import tkinter as tk

from Field import FIELD
from Window import Window

from constants import CELL_SIZE


class Canvas:
    def __init__(self, field):
        self.map = field
        self.cell_size = CELL_SIZE
        self.canvas = self.init_canvas()
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def init_canvas(self):
        width = len(self.map[0])
        height = len(self.map)

        canvas_width = width * self.cell_size
        canvas_height = height * self.cell_size

        Window.config(
            width=canvas_width,
            height=canvas_height
        )

        Window.resizable(
            width=False,
            height=False
        )git

        canvas = tk.Canvas(Window,
                        width=canvas_width,
                        height=canvas_height,
                        bg='black')
        return canvas


CANVAS = Canvas(FIELD).canvas


