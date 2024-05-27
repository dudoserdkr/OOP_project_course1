from tkinter import *
from PIL import ImageTk, Image

from Coin import Coin
from Canvas import CANVAS
from constants import CELL_SIZE

class Tablet(Coin):
    CELL_SIZE = 20

    def __init__(self, position):
        super().__init__(position)
        self.picture = Image.open("pictures/tablet.png")
        self.resized = ImageTk.PhotoImage(
            self.picture.resize((Tablet.CELL_SIZE, Tablet.CELL_SIZE), Image.Resampling.LANCZOS))
        self.tablet_position = [position[0] * CELL_SIZE, position[1] * CELL_SIZE]
        self.position = [position[1], position[0]]
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

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update_score(Coin.SCORE)

    def change_status(self, pacman):

        if pacman.position == self.position and self.TABLET_STATUS:
            self.TABLET_STATUS = False
            Coin.SCORE += 50
            self.notify_observers()
            self.delete()
