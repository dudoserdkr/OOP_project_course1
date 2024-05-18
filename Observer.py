from Coin import Coin
from Tablet import Tablet
from VisualPacMan import VisualPacMan
from Window import Window
from Field import FIELD
from FieldDrawing import FieldDrawing
from Score import Score
from VisualScore import VisualScore
from constants import DELAY
from PacmanCoinsTablets import PacmanCoinsTablets


class Observer:
    def __init__(self, pacman):
        self.observers = []
        self.pacman = pacman

    def __add__(self, other):
        self.observers.append(other)

    def main_loop(self):
        for observer in self.observers:
            observer.get_pacman_pos(self.pacman)

        Window.after(DELAY // 30, lambda: self.main_loop())


if __name__ == '__main__':
    total = PacmanCoinsTablets()
    ob = Observer(total.vp)
    # Додали підписника який отримує інфу про позицію пакмана, подімна штука буде і з гостами
    ob + total
    total.pacman()
    ob.main_loop()

    # total.map()
    total.coin()
    total.tablet_list_maker()
    total.tablet_drawer()
    total.score_coin()
    total.score_tablet()
    total.scoreboard()

    Window.mainloop()
