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
            obs.get_pacman(self.pacman)
        if not any([self.total.coin_list, self.total.tablet_list]):
            print("Got all coins and tablets!")
            total.coin_tablet_total()

        Window.after(DELAY // 30, lambda: self.main_loop())


if __name__ == '__main__':
    total = Total()
    observer = Observer(total, total.vp)
    observer.main_loop()
    observer + total

    Window.mainloop()
