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
        self.canvas.bind("<Motion>", self.show_coordinates)  # Привязываем событие движения мыши к обработчику

        self.coord_label = Label(Window, text="", bg="white")
        self.coord_label.pack(side=BOTTOM)  # Располагаем метку внизу окна

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
                    color = "pink"
                elif self.map[i][j] == 3:
                    color = "pink"
                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="gray"
                )
        self.canvas.pack()

    def show_coordinates(self, event):
        # Определяем координаты клетки, на которую наведена мышь
        x, y = event.x, event.y
        col = x // self.cell_size
        row = y // self.cell_size

        # Проверяем, что координаты клетки находятся в пределах карты
        if 0 <= col < len(self.map[0]) and 0 <= row < len(self.map):
            self.coord_label.config(text=f"Coordinates: ({col}, {row})")
        else:
            self.coord_label.config(text="")  # Если координаты вне карты, очищаем метку


if __name__ == '__main__':
    m = FieldDrawing(FIELD)
    m.draw_field()
    Window.mainloop()
