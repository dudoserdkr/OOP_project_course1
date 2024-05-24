from Window import Window

from constants import DELAY
from Total import Total


class Observer:
    def __init__(self, total, pacman):
        self.observers = []
        self.pacman = pacman
        self.total = total

    def __add__(self, other):
        self.observers.append(other)

    def main_loop(self):
        for obs in self.observers:
            obs.get_pacman_pos(self.pacman)
        if not any([self.total.coin_list, self.total.tablet_list]):
            print("Все монеты и таблетки собраны!")
            total.coin_tablet_total()

        Window.after(DELAY // 30, lambda: self.main_loop())






if __name__ == '__main__':
    total = Total()
    observer = Observer(total, total.vp)
    # Додали підписника який отримує інфу про позицію пакмана, подімна штука буде і з гостами


    observer.main_loop()

    observer + total
    total.pacman()
    #total.coin_tablet_total()
    total.score_coin()
    total.score_tablet()
    total.scoreboard()

    Window.mainloop()
