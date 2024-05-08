from Object import Object
from Field import Field
from Window import Window
from FieldDrawing import FieldDrawing
import random


class Ghost(Object):
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
    def move_left(self):
        (curr_y, curr_x) = self.position
        if self.map[curr_y + 1][curr_x] == 1:
            return
        self.position[0] += 1
        self.data_of_last_move = 1
    def move_right(self):
        (curr_y, curr_x) = self.position
        if self.map[curr_y - 1][curr_x] == 1:
            return
        self.position[0] += 1
        self.data_of_last_move = 2
    def move_up(self):
        (curr_y, curr_x) = self.position
        if self.map[curr_y][curr_x + 1] == 1:
            return
        self.position[0] += 1
        self.data_of_last_move = 3
    def move_down(self):
        (curr_y, curr_x) = self.position
        if self.map[curr_y][curr_x - 1] == 1:
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
    def move(self): #random move
        list_of_possibilities = []
        left_step_poss = self.map[self.position[0] - 1][self.position[1]]
        if left_step_poss == 1:
            list_of_possibilities.append(1)
        right_step_poss = self.map[self.position[0] + 1][self.position[1]]
        if right_step_poss == 1:
            list_of_possibilities.append(2)
        up_step_poss = self.map[self.position[0]][self.position[1] + 1]
        if up_step_poss == 1:
            list_of_possibilities.append(3)
        down_step_poss = self.map[self.position[0]][self.position[1] - 1]
        if down_step_poss == 1:
            list_of_possibilities.append(4)
        if self.data_of_last_move in list_of_possibilities:
            list_of_possibilities.remove(self.data_of_last_move)
        number_vector = random.choice(list_of_possibilities)
        if number_vector == 1:
            self.move_left()
        elif number_vector == 2:
            self.move_right()
        elif number_vector == 3:
            self.move_up()
        elif number_vector == 4:
            self.move_down()

