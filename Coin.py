from tkinter import *
from PIL import ImageTk, Image

from Canvas import CANVAS
from Window import Window
from Field import FIELD
from FieldDrawing import FieldDrawing#
from Canvas import CANVAS


class Coin:
    COIN_STATUS = True
    CELL_SIZE = 5

    #CANVAS_POSITION = [13 * 20, 23 * 20]
    def __init__(self, position):
        self.picture = Image.open("pictures/quadratico.png ")
        self.coin_position = [position[0] * 20, position[1] * 20]
        self.score_counter = 0
    def draw(self):
        if Coin.COIN_STATUS == True:
            image = self.picture
            resized_image = image.resize((Coin.CELL_SIZE , Coin.CELL_SIZE ), Image.Resampling.LANCZOS)
            self.coin_picture = ImageTk.PhotoImage(resized_image)
            id = CANVAS.create_image(self.coin_position[0] + 10, self.coin_position[1] + 10,
                                     image=self.coin_picture)
            return id

        return id
    def change_status(self, pacman):
        if pacman.position == self.coin_position:
            Coin.COIN_STATUS = False
            self.score_counter += 10


if __name__ == "__main__":
    m = FieldDrawing(FIELD)
    m.draw_field()
    #c = Coin((1, 1) )
    #c.draw()
    #Window.mainloop()


    ex = []
    for i in range(0, 28):
        for e in range(0, 30):
            c = Coin((i, e))
            if FIELD[e][i] == 0 and not (20 > e > 8 and 21 > i > 6):
                #c.draw()
                ex.append(c)
    for t in ex:
        t.draw()
    Window.mainloop()









