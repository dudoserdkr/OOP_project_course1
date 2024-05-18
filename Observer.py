from Window import Window

from constants import DELAY
from Total import Total


class Observer:
    def __init__(self, pacman):
        self.observers = []
        self.pacman = pacman

    def __add__(self, other):
        self.observers.append(other)

    def main_loop(self):
        for obs in self.observers:
            obs.get_pacman_pos(self.pacman)

        Window.after(DELAY // 30, lambda: self.main_loop())


if __name__ == '__main__':
    total = Total()
    observer = Observer(total.vp)
    # Додали підписника який отримує інфу про позицію пакмана, подімна штука буде і з гостами
    observer + total
    total.pacman()
    observer.main_loop()
    total.coin()
    total.tablet_list_maker()
    total.tablet_drawer()
    total.score_coin()
    total.score_tablet()
    total.scoreboard()

    Window.mainloop()
