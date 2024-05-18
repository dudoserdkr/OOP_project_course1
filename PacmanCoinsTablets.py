from Coin import Coin
from Tablet import Tablet
from VisualPacMan import VisualPacMan
from Window import Window
from Field import FIELD
from FieldDrawing import FieldDrawing
from Score import Score
from VisualScore import VisualScore
import tkinter as tk


class PacmanCoinsTablets:
    DELAY = 30

    def __init__(self):
        self.first_tablet = Tablet([1, 3])
        self.second_tablet = Tablet([1, 23])
        self.third_tablet = Tablet([26, 3])
        self.fourth_tablet = Tablet([26, 23])
        self.coin_list = []
        self.tablet_list = []
        self.score = Score()

        self.pacman_pos = None
        self.vp = VisualPacMan()

    def get_pacman_pos(self, pacman):
        self.coin_check(pacman)
        self.tablet_check(pacman)

    def coin_check(self, pacman):
        for coin in self.coin_list:
            coin.change_status(pacman)

    def tablet_check(self, pacman):
        for tablet in self.tablet_list:
            tablet.change_status(pacman)

    # def coin_check(self, pacman, coin_list):
    #     for coin in coin_list:
    #         coin.change_status(pacman)
    #     Window.after(PacmanCoinsTablets.DELAY // 30, lambda: self.coin_check(pacman, coin_list))
    #
    # def tablet_check(self, pacman, tablet_list):
    #     for tablet in tablet_list:
    #         tablet.change_status(pacman)
    #     Window.after(PacmanCoinsTablets.DELAY // 30, lambda: self.tablet_check(pacman, tablet_list))

    @staticmethod
    def map():
        field = FieldDrawing(FIELD)
        field.draw_field()

    def coin(self):
        for i in range(0, 28):
            for e in range(0, 30):
                c = Coin([i, e])
                if FIELD[e][i] == 0 and not (20 > e > 8 and 21 > i > 6) and not (i == 1 and e == 3) and not (i == 1 and e == 23) and not (i == 26 and e == 3) and not (i == 26 and e == 23) and not (e == 14):
                    self.coin_list.append(c)
        for t in self.coin_list:
            t.draw()

    def score_coin(self):
        for t in self.coin_list:
            t.register_observer(self.score)

    def tablet_list_maker(self):
        self.tablet_list = []
        self.tablet_list.append(self.first_tablet)
        self.tablet_list.append(self.second_tablet)
        self.tablet_list.append(self.third_tablet)
        self.tablet_list.append(self.fourth_tablet)

    def tablet_drawer(self):
        self.first_tablet.draw()
        self.second_tablet.draw()
        self.third_tablet.draw()
        self.fourth_tablet.draw()

    def score_tablet(self):
        self.first_tablet.register_observer(self.score)
        self.second_tablet.register_observer(self.score)
        self.third_tablet.register_observer(self.score)
        self.fourth_tablet.register_observer(self.score)

    def scoreboard(self):
        vs = VisualScore()
        self.score.register_listener(vs)
        return vs

    def pacman(self):
        # vp = VisualPacMan()
        # self.coin_check(vp, self.coin_list)
        # self.tablet_check(vp, self.tablet_list)
        # vp = VisualPacMan()
        self.coin_check(self.vp)
        self.tablet_check(self.vp)
        Window.bind('<Left>', self.vp.move_left)
        Window.bind('<Right>', self.vp.move_right)
        Window.bind('<Up>', self.vp.move_up)
        Window.bind('<Down>', self.vp.move_down)


if __name__ == '__main__':
    vp = VisualPacMan()
    total = PacmanCoinsTablets()
    total.map()
    total.coin()
    total.tablet_list_maker()
    total.tablet_drawer()
    total.score_coin()
    total.score_tablet()
    total.scoreboard()
    total.pacman()
    Window.mainloop()




