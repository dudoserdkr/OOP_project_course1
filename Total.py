from Coin import Coin
from Tablet import Tablet
from VisualPacMan import VisualPacMan
from FieldDrawing import FieldDrawing
from Score import Score
from VisualScore import VisualScore
from Field import FIELD


class Total:
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
        self.map = self.map()
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

    @staticmethod
    def map():
        field = FieldDrawing(FIELD)
        field.draw_field()

    def coin(self):
        for i in range(0, 28):
            for e in range(0, 30): # TODO: FIELD_HEIGHT, FIELD_WIDTH
                c = Coin([i, e]) # TODO: make few strings for if instead of one
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
        for tab in self.tablet_list:
            tab.draw()

    def score_tablet(self):
        for tab in self.tablet_list:
            tab.register_observer(self.score)

    def scoreboard(self):
        vs = VisualScore()
        self.score.register_listener(vs)

    def pacman(self):
        self.coin_check(self.vp)
        self.tablet_check(self.vp)





