from Window import Window
from FieldDrawing import FieldDrawing
import random


class Ghost:
    def __init__(self, position, pic_right_1, pic_right_2, pic_left_1, pic_left_2, pic_up_1,  pic_up_2, pic_down_1, pic_down_2):
        self.FUCKING_EXIT1 = (14, 21)
        self.FUCKING_EXIT2 = (15, 21)
        self.data_of_last_move = 0
        self.position = position
        self.pic_right_1 = pic_right_1
        self.pic_right_2 = pic_right_2
        self.pic_left_1 = pic_left_1
        self.pic_left_2 = pic_left_2
        self.pic_up_1 = pic_up_1
        self.pic_up_2 = pic_up_2
        self.pic_down_1 = pic_down_1
        self.pic_down_2 = pic_down_2

    def move_left(self, map):
        (curr_y, curr_x) = self.position
        if map[curr_y + 1][curr_x] == 1: #self.map is wrong
            return
        self.position[0] += 1
        self.data_of_last_move = 1

    def move_right(self, map):
        (curr_y, curr_x) = self.position
        if map[curr_y - 1][curr_x] == 1:
            return
        self.position[0] += 1
        self.data_of_last_move = 2

    def move_up(self, map):
        (curr_y, curr_x) = self.position
        if map[curr_y][curr_x + 1] == 1:
            return
        self.position[0] += 1
        self.data_of_last_move = 3

    def move_down(self, map):
        (curr_y, curr_x) = self.position
        if map[curr_y][curr_x - 1] == 1:
            return
        self.position[0] += 1
        self.data_of_last_move = 4

    def drawer(self):
        FieldDrawing.draw_field()
        # the picture will be chosen after the choice of the last move
        #pacman_id = canvas.create_image(self.position[0] + 10, self.position[1] + 10, image=pacman_photo)

    def entrance_field(self): #the entrance of the spawn
        first_diff = (self.FUCKING_EXIT1[0] - self.position[0], self.FUCKING_EXIT1[1] - self.position[1]) #to which of two positions on the entrance should we go
        second_diff = (self.FUCKING_EXIT2[0] - self.position[0], self.FUCKING_EXIT2[1] - self.position[1])
        if first_diff[0] == 0: #going just ahead
            for i in range(first_diff[1]):
                self.move_up()
                self.drawer()
        elif second_diff[0] == 0: #going just ahead
            for i in range(second_diff[1]):
                self.move_up()
                self.drawer()
        elif abs(first_diff) > abs(second_diff):
            for i in range(first_diff[0]):
                self.move_right()
                self.drawer()
            for i in range(first_diff[1]):
                self.move_up()
                self.drawer()
        elif abs(first_diff) < abs(second_diff):
            for i in range(second_diff[0]):
                self.move_left()
                self.drawer()
            for i in range(first_diff[1]):
                self.move_up()
                self.drawer()

    def possibilities_list_maker(self, map): #random move
        list_of_possibilities = []
        left_step_poss = map[self.position[0] - 1][self.position[1]]
        if left_step_poss == 1:
            list_of_possibilities.append(1)
        right_step_poss = map[self.position[0] + 1][self.position[1]]
        if right_step_poss == 1:
            list_of_possibilities.append(2)
        up_step_poss = map[self.position[0]][self.position[1] + 1]
        if up_step_poss == 1:
            list_of_possibilities.append(3)
        down_step_poss = map[self.position[0]][self.position[1] - 1]
        if down_step_poss == 1:
            list_of_possibilities.append(4)
        if self.data_of_last_move in list_of_possibilities:
            list_of_possibilities.remove(self.data_of_last_move)
            return list_of_possibilities
    def move_regime_random(self, map):
        list_of_possibilities = self.possibilities_list_maker(map)
        number_vector = random.choice(list_of_possibilities)
        if number_vector == 1:
            self.move_left()
            self.drawer()
        elif number_vector == 2:
            self.move_right()
            self.drawer()
        elif number_vector == 3:
            self.move_up()
            self.drawer()
        elif number_vector == 4:
            self.move_down()
            self.drawer()

    def move_regime_predator(self, map, pacman):
        list_of_possibilities = self.possibilities_list_maker(map)
        list_of_hyps = []
        hyp1 = 0
        hyp2 = 0
        hyp3 = 0
        hyp4 = 0
        for i in list_of_possibilities:
            if i == 1:
                x = pacman.position[0]  # we build a 90gr. triangle
                y = self.position[1]
                katet1 = ((pacman.position[1] - y) ** 2) ** 0.5  # length
                katet2 = ((self.position[0] - 1 - x) ** 2) ** 0.5
                hyp1 = ((katet1 ** 2) + (katet2 ** 2)) ** 0.5

            elif i == 2:
                x = pacman.position[0]  # we build a 90gr. triangle
                y = self.position[1]
                katet1 = ((pacman.position[1] - y) ** 2) ** 0.5  # length
                katet2 = ((self.position[0] + 1 - x) ** 2) ** 0.5
                hyp1 = ((katet1 ** 2) + (katet2 ** 2)) ** 0.5
                #list_of_hyps.append(hyp1)
            elif i == 3:
                x = pacman.position[0]  # we build a 90gr. triangle
                y = self.position[1]
                katet1 = ((pacman.position[1] + 1 - y) ** 2) ** 0.5  # length
                katet2 = ((self.position[0] - x) ** 2) ** 0.5
                hyp1 = ((katet1 ** 2) + (katet2 ** 2)) ** 0.5
                #list_of_hyps.append(hyp1)
            elif i == 1:
                x = pacman.position[0]  # we build a 90gr. triangle
                y = self.position[1]
                katet1 = ((pacman.position[1] - 1 - y) ** 2) ** 0.5  # length
                katet2 = ((self.position[0] - 1 - x) ** 2) ** 0.5
                hyp1 = ((katet1 ** 2) + (katet2 ** 2)) ** 0.5
                #list_of_hyps.append(hyp1)
            list_of_hyps.append(hyp1)
            list_of_hyps.append(hyp2)
            list_of_hyps.append(hyp3)
            list_of_hyps.append(hyp4)

        keys = [1, 2, 3, 4]
        my_dict = dict.fromkeys(keys, None)
        my_dict[1] = hyp1
        my_dict[2] = hyp2
        my_dict[3] = hyp3
        my_dict[4] = hyp4
        max_key = max(my_dict, key=my_dict.get)
        if max_key == 1:
            self.move_left()
            self.drawer()
        elif max_key == 2:
            self.move_right()
            self.drawer()
        elif max_key == 3:
            self.move_up()
            self.drawer()
        elif max_key == 4:
            self.move_down()
            self.drawer()

    def move_regime_chooser(self, pacman): #here we find length between pacman and ghost, if this length is too short, ghost switches to regime of predator
        x = pacman.position[0] #we build a 90gr. triangle
        y = self.position[1]
        katet1 = ((pacman.position[1] - y) ** 2) ** 0.5 #length
        katet2 = ((self.position[0] - x) ** 2) ** 0.5
        hyp = ((katet1 ** 2) + (katet2 ** 2)) ** 0.5
        if hyp <= 5:
               self.move_regime_predator(pacman)
        else:
            self.move_regime_random(pacman)