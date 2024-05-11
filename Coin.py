from tkinter import *
from PIL import ImageTk, Image
from VisualPacMan import VisualPacMan
from Canvas import CANVAS
from Window import Window
from Field import FIELD
from FieldDrawing import FieldDrawing
from Canvas import CANVAS
from constants import DELAY, CELL_SIZE


class Coin:
    COIN_STATUS = True
    CELL_SIZE = 5

    #CANVAS_POSITION = [13 * 20, 23 * 20]
    def __init__(self, position):
        self.picture = Image.open("pictures/quadratico.png ")
        self.resized = ImageTk.PhotoImage(self.picture.resize((Coin.CELL_SIZE, Coin.CELL_SIZE), Image.Resampling.LANCZOS))
        self.coin_position = [position[0] * CELL_SIZE, position[1] * CELL_SIZE]
        self.position = [position[1], position[0]]  # МАТЕМАТИЧНА ПОЗИЦІЯ
        self.score_counter = 0
        self.id = None

    def draw(self):
        if Coin.COIN_STATUS == True:
            self.id = CANVAS.create_image(self.coin_position[0] + 10, self.coin_position[1] + 10, image=self.resized)
        return

    def delete(self):
        CANVAS.delete(self.id)

    def change_status(self, pacman):
        if pacman.position == self.position:
            Coin.COIN_STATUS = False
            self.delete()
            self.score_counter += 10


def coin_check(pacman, coin_list):
    print(f"Pacman {pacman.position}")
    for coin in coin_list:
        coin.change_status(pacman)
        # print(f"Coin: {coin.position}")

    Window.after(DELAY // 30, lambda: coin_check(pacman, coin_list))




if __name__ == "__main__":
    m = FieldDrawing(FIELD)
    m.draw_field()
    #c = Coin((1, 1) )
    #c.draw()
    #Window.mainloop()


    ex = []
    for i in range(0, 28):
        for e in range(0, 30):
            c = Coin([i, e])  # СПИСОК
            if FIELD[e][i] == 0 and not (20 > e > 8 and 21 > i > 6):
                #c.draw()
                ex.append(c)
    for t in ex:
        t.draw()

    vp = VisualPacMan()
    coin_check(vp, ex)
    Window.bind('<Left>', vp.move_left)
    Window.bind('<Right>', vp.move_right)
    Window.bind('<Up>', vp.move_up)
    Window.bind('<Down>', vp.move_down)
    Window.mainloop()









