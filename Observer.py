from Window import Window
import tkinter as tk
from PIL import Image, ImageTk

from Ghost_logic.Blinky import Blinky
from Ghost_logic.Pinky import Pinky
from Ghost_logic.Inky import Inky
from Ghost_logic.Clyde import Clyde
from Ghost_logic.GhostDrawer import GhostDrawer
from random import randint
from constants import DELAY
from Total import Total
from Canvas import CANVAS



class Observer:
    def __init__(self, total, pacman, blinky):
        self.observers = []
        self.pacman = pacman
        self.total = total
        self.blinky = blinky

    def __add__(self, other):
        self.observers.append(other)
        return self

    def main_loop(self):
        for obs in self.observers:
            obs.set_pacman(self.pacman)
            if type(obs) == Inky and randint(0, 100) == 55:
                obs.set_blinky(self.blinky)
                del obs
        if not any([self.total.coin_list, self.total.tablet_list]):
            print("Got all coins and tablets!")
            total.coin_tablet_total()
        if self.pacman.available_lives == 0:
            game_over_window = tk.Toplevel()
            game_over_window.title("Game Over")
            game_over_window.geometry("200x150+310+300")
            photo = Image.open("pictures/game_over.jpg")
            photo_normal = photo.resize((210, 150), Image.Resampling.LANCZOS)
            photo_normal_tk = ImageTk.PhotoImage(photo_normal)
            image_label = tk.Label(game_over_window, image=photo_normal_tk)
            image_label.pack(side=tk.RIGHT, padx=(0, 20))
            image_label.image = photo_normal_tk
            game_over_window.eval('tk::PlaceWindow . center')
            CANVAS.pack_forget()  #???
            return
        Window.after(DELAY // 30, lambda: self.main_loop())


if __name__ == '__main__':
    total = Total()
    b = Blinky()
    i = Inky()
    p = Pinky()
    c = Clyde()
    observer = Observer(total, total.vp, b)
    observer + total + i + p + c


    d1 = GhostDrawer(b)
    d2 = GhostDrawer(i)
    d3 = GhostDrawer(p)
    d4 = GhostDrawer(c)

    observer.main_loop()

    d1.draw()
    d2.draw()
    d3.draw()
    d4.draw()

    Window.mainloop()
