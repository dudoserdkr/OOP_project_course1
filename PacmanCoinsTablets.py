from Coin import Coin
from Tablet import Tablet
from VisualPacMan import VisualPacMan
from Window import Window
from Field import FIELD
from FieldDrawing import FieldDrawing
from Score import Score


class PacmanCoinsTablets:
    DELAY = 30

    def __init__(self):
        self.first_tablet = Tablet([1, 3])
        self.second_tablet = Tablet([1, 23])
        self.third_tablet = Tablet([26, 3])
        self.fourth_tablet = Tablet([26, 23])
        self.coin_list = []
        self.tablet_list = []

    def coin_check(self, pacman, coin_list):
        for coin in coin_list:
            coin.change_status(pacman)

        Window.after(PacmanCoinsTablets.DELAY // 30, lambda: self.coin_check(pacman, coin_list))

    def tablet_check(self, pacman, tablet_list):
        # print(f"Pacman {pacman.position}")
        for tablet in tablet_list:
            tablet.change_status(pacman)

        Window.after(PacmanCoinsTablets.DELAY // 30, lambda: self.tablet_check(pacman, tablet_list))

    @staticmethod

    def map():
        field = FieldDrawing(FIELD)
        field.draw_field()

    def coin(self):
        for i in range(0, 28):
            for e in range(0, 30):
                c = Coin([i, e])
                if FIELD[e][i] == 0 and not (20 > e > 8 and 21 > i > 6) and not (i == 1 and e == 3) and not (
                        i == 1 and e == 23) and not (i == 26 and e == 3) and not (i == 26 and e == 23):

                    self.coin_list.append(c)
        for t in self.coin_list:
            t.draw()

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

    def score(self):
        score = Score()
        self.first_tablet.register_observer(score)
        self.second_tablet.register_observer(score)
        self.third_tablet.register_observer(score)
        self.fourth_tablet.register_observer(score)

    def pacman(self):
        vp = VisualPacMan()
        self.coin_check(vp, self.coin_list)
        self.tablet_check(vp, self.tablet_list)
        Window.bind('<Left>', vp.move_left)
        Window.bind('<Right>', vp.move_right)
        Window.bind('<Up>', vp.move_up)
        Window.bind('<Down>', vp.move_down)
        Window.mainloop()

if __name__ == '__main__':
    total = PacmanCoinsTablets()
    total.map()
    total.coin()
    total.tablet_list_maker()
    total.tablet_drawer()
    total.score()
    total.pacman()


