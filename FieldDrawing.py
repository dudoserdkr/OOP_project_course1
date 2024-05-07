from tkinter import *

from Field import Field
from Window import Window

from constants import CELL_SIZE


class FieldDrawing:
    def __init__(self, field):
        self.map = field
        self.cell_size = CELL_SIZE
        self.canvas = self.init_canvas()

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
        )

        canvas = Canvas(Window,
                        width=canvas_width,
                        height=canvas_height,
                        bg='black'
                        )
        return canvas

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
    field = Field()
    m = FieldDrawing(field.map)
    m.draw_field()
    Window.mainloop()
