from tkinter import *

from Field import FIELD
from Window import Window

from Canvas import CANVAS

from constants import CELL_SIZE


class FieldDrawing:
    def __init__(self, field):
        self.map = field
        self.cell_size = CELL_SIZE
        self.canvas = CANVAS

    def draw_field(self):
        width = len(self.map[0])
        height = len(self.map)

        color = ''

        for i in range(height):
            for j in range(width):
                x1, y1 = j * self.cell_size, i * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                if self.map[i][j] == 1:
                    color = "blue"
                elif self.map[i][j] == 0:
                    color = "black"
                elif self.map[i][j] == 2:
                    color = "blue"
                elif self.map[i][j] == 3:
                    color = "pink"
                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="gray"
                )
        self.canvas.pack()


if __name__ == '__main__':
    m = FieldDrawing(FIELD)
    m.draw_field()
    Window.mainloop()