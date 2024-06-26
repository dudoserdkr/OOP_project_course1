from Coin import Coin
from Tablet import Tablet
from VisualPacMan import VisualPacMan
from FieldDrawing import FieldDrawing
from Score import Score
from VisualScore import VisualScore
from Field import FIELD

from PIL import ImageTk, Image

import pygame
import threading

pygame.init()
pygame.mixer.init()


class Total:
    DELAY = 30

    def __init__(self):
        self.coin_list = []
        self.tablet_list = []
        self.score = Score()
        self.vs = VisualScore()
        self.pacman_pos = None
        self.map()
        self.score_coin()
        self.score_tablet()
        self.scoreboard()
        self.observers = []
        self.empty_field = True
        self.vp = VisualPacMan()
        self.lives = 3
        self.image_chooser()
        self.sound_channel = pygame.mixer.Channel(1)

    def set_pacman(self, pacman):
        # TODO: stop using Get_pacman_pos and remake all up to this method
        self.check_score_attributes(pacman)
        if self.vp.available_lives != self.lives:
            self.lives = self.vp.available_lives
            self.image_chooser()
            self.sound()

    def sound(self):
        def play_sound():
            if self.sound_channel.get_busy():
                self.sound_channel.stop()

            sound = pygame.mixer.Sound("sound/death.wav")
            self.sound_channel.play(sound)
            while self.sound_channel.get_busy():
                pygame.time.delay(100)
        threading.Thread(target=play_sound).start()


    def check_score_attributes(self, pacman):
        self.coin_check(pacman)
        self.tablet_check(pacman)

    def image_chooser(self):
        photo = None
        if self.vp.available_lives == 3:
            photo = Image.open("pictures/three_pacmans_first.png")
            photo_normal = photo.resize((120, 40), Image.Resampling.LANCZOS)
        elif self.vp.available_lives == 2:
            photo = Image.open("pictures/two_pacmans_first.png")
            photo_normal = photo.resize((80, 40), Image.Resampling.LANCZOS)
        elif self.vp.available_lives == 1:
            photo = Image.open("pictures/one_pacmans_first.png")
            photo_normal = photo.resize((40, 40), Image.Resampling.LANCZOS)
        elif self.vp.available_lives == 0:
            photo = Image.open("pictures/no_pacmans_first.png")
            photo_normal = photo.resize((110, 40), Image.Resampling.LANCZOS)
        self.vs.image_chooser(photo_normal)

    def coin_tablet_total(self):
        if not self.coin_list and not self.tablet_list:
            self.coin()
            self.tablet_list_maker()
            self.tablet_drawer()
            self.score_coin()
            self.score_tablet()


    def coin_check(self, pacman):
        for coin in self.coin_list:
            coin.change_status(pacman)
            if not coin.COIN_STATUS:
                try:
                    self.coin_list.remove(coin)
                except ValueError:
                    pass

    def tablet_check(self, pacman):
        for tablet in self.tablet_list:
            tablet.change_status(pacman)
            if not tablet.TABLET_STATUS:
                try:
                    self.tablet_list.remove(tablet)
                except ValueError:
                    pass

    @staticmethod
    def map():
        field = FieldDrawing(FIELD)
        field.draw_field()

    def coin(self):
        for i in range(0, 28):
            for e in range(0, 30):
                c = Coin([i, e])
                if (FIELD[e][i] == 0 and not (20 > e > 8 and 21 > i > 6) and not (i == 1 and e == 3)
                        and not (i == 1 and e == 23) and not (i == 26 and e == 3) and not
                        (i == 26 and e == 23) and not (e == 14)):
                    self.coin_list.append(c)
        for t in self.coin_list:
            t.draw()

    def score_coin(self):
        for t in self.coin_list:
            t.register_observer(self.score)

    def tablet_list_maker(self):
        first_tablet = Tablet([1, 3])
        second_tablet = Tablet([1, 23])
        third_tablet = Tablet([26, 3])
        fourth_tablet = Tablet([26, 23])
        self.tablet_list = []
        self.tablet_list.append(first_tablet)
        self.tablet_list.append(second_tablet)
        self.tablet_list.append(third_tablet)
        self.tablet_list.append(fourth_tablet)

    def tablet_drawer(self):
        for tab in self.tablet_list:
            tab.draw()

    def score_tablet(self):
        for tab in self.tablet_list:
            tab.register_observer(self.score)

    def scoreboard(self):
        self.score.register_listener(self.vs)

    def pacman(self):
        self.coin_check(self.vp)
        self.tablet_check(self.vp)
