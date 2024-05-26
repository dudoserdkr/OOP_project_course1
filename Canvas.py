import tkinter as tk

from Field import FIELD
from Window import Window

from constants import CELL_SIZE


def create_canvas(window, field_width, field_height) -> tk.Canvas:
    window.config(
        width=field_width,
        height=field_height
    )

    window.resizable(
        width=True,
        height=True
    )

    canvas = tk.Canvas(
        window,
        width=field_width,
        height=field_height,
        bg='black'
    )
    canvas.pack(fill=tk.BOTH, expand=True)

    return canvas


field_width = len(FIELD[0]) * CELL_SIZE
field_height = len(FIELD) * CELL_SIZE


CANVAS = create_canvas(Window, field_width, field_height)
