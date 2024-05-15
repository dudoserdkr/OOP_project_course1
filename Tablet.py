from Coin import Coin
from tkinter import *
from PIL import ImageTk, Image
from VisualPacMan import VisualPacMan
from Canvas import CANVAS
from Window import Window
from Field import FIELD
from FieldDrawing import FieldDrawing
from Canvas import CANVAS
from constants import DELAY, CELL_SIZE

class Tablet(Coin):
    CELL_SIZE = 20

    def __init__(self, position):
        super().__init__(position)
        self.picture = Image.open("pictures/tablet.png")
        self.resized = ImageTk.PhotoImage(
            self.picture.resize((Tablet.CELL_SIZE, Tablet.CELL_SIZE), Image.Resampling.LANCZOS))
        self.tablet_position = [position[0] * CELL_SIZE, position[1] * CELL_SIZE]
        self.position = [position[1], position[0]]  # МАТЕМАТИЧНА ПОЗИЦІЯ
        self.score_counter = 0
        self.id = None
        self._observers = []
        self.TABLET_STATUS = True

    def draw(self):
        self.id = CANVAS.create_image(self.tablet_position[0] + 10, self.tablet_position[1] + 10, image=self.resized)

    def register_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
            observer.update_score(Coin.SCORE)
            print("registered observer")
    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update_score(Coin.SCORE)

    def change_status(self, pacman):

        if pacman.position == self.position and self.TABLET_STATUS:
            self.TABLET_STATUS = False  # Змінюємо статус на "неактивна"
            #self.delete()  # Видаляємо монетку з ігрового поля
            Coin.SCORE += 50  # Збільшуємо рахунок
            self.notify_observers()
            self.delete()


def coin_check(pacman, coin_list):
    print(f"Pacman {pacman.position}")
    for coin in coin_list:
        coin.change_status(pacman)
        # print(f"Coin: {coin.position}")

    Window.after(DELAY // 30, lambda: coin_check(pacman, coin_list))

def tablet_check(pacman, tablet_list):
    print(f"Pacman {pacman.position}")
    for tablet in tablet_list:
        tablet.change_status(pacman)
        # print(f"Coin: {coin.position}")

    Window.after(DELAY // 30, lambda: tablet_check(pacman, tablet_list))


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
            if FIELD[e][i] == 0 and not (20 > e > 8 and 21 > i > 6) and not (i == 1 and e == 3) and not (i == 1 and e == 23) and not (i == 26 and e == 3) and not (i == 26 and e == 23):
                #c.draw()
                ex.append(c)
    nex = []
    for t in ex:
        t.draw()

    first_tablet = Tablet([1, 3])
    nex.append(first_tablet)
    second_tablet = Tablet([1, 23])
    nex.append(second_tablet)
    third_tablet = Tablet([26, 3])
    nex.append(third_tablet)
    fourth_tablet = Tablet([26, 23])
    nex.append(fourth_tablet)

    first_tablet.draw()
    second_tablet.draw()
    third_tablet.draw()
    fourth_tablet.draw()

    vp = VisualPacMan()
    coin_check(vp, ex)
    tablet_check(vp, nex)
    Window.bind('<Left>', vp.move_left)
    Window.bind('<Right>', vp.move_right)
    Window.bind('<Up>', vp.move_up)
    Window.bind('<Down>', vp.move_down)
    Window.mainloop()

