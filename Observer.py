from Window import Window

from Ghost_logic.Blinky import Blinky
from Ghost_logic.Pinky import Pinky
from Ghost_logic.Inky import Inky
from Ghost_logic.Clyde import Clyde
from Ghost_logic.GhostDrawer import GhostDrawer

from constants import DELAY
from Total import Total


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
            if type(obs) == Inky:
                obs.set_blinky(self.blinky)
        if not any([self.total.coin_list, self.total.tablet_list]):
            print("Got all coins and tablets!")
            total.coin_tablet_total()

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
