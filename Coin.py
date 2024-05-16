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
    SCORE = 0

    #CANVAS_POSITION = [13 * 20, 23 * 20]
    def __init__(self, position):
        self.picture = Image.open("pictures/quadratico.png")
        self.resized = ImageTk.PhotoImage(self.picture.resize((Coin.CELL_SIZE, Coin.CELL_SIZE), Image.Resampling.LANCZOS))
        self.coin_position = [position[0] * CELL_SIZE, position[1] * CELL_SIZE]
        self.position = [position[1], position[0]]  # МАТЕМАТИЧНА ПОЗИЦІЯ
        self.COIN_STATUS = True
        self.id = None
        self.observers = []

    def draw(self):
        self.id = CANVAS.create_image(self.coin_position[0] + 10, self.coin_position[1] + 10, image=self.resized)

    def delete(self):
        CANVAS.delete(self.id)

    def register_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
            observer.update_score(Coin.SCORE)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update_score(Coin.SCORE)
            print ("notified observers")



    def status(self):
        if not self.COIN_STATUS:
            self.notify_observers()

    def change_status(self, pacman):
        if pacman.position == self.position and self.COIN_STATUS:
            self.COIN_STATUS = False
            #self.delete()
            Coin.SCORE += 10
            self.notify_observers()
            self.delete()



def coin_check(pacman, coin_list):
    for coin in coin_list:
        coin.change_status(pacman)
    Window.after(DELAY // 30, lambda: coin_check(pacman, coin_list))




