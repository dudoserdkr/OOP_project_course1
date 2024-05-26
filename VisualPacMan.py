from tkinter import *
from PIL import ImageTk, Image

from PacMan import PacMan
from FieldDrawing import FieldDrawing

from Window import Window
from Field import FIELD, SPECIAL_POS_1, SPECIAL_POS_2
from constants import CELL_SIZE, DELAY, ANIMATION_STEP, ANIMATION_STEP_SIZE
from Canvas import CANVAS


class VisualPacMan(PacMan):
    def __init__(self):
        super().__init__()
        self.canvas = CANVAS
        # self.absolut_speed = DELAY / self.speed
        self.canvas_position = [13 * CELL_SIZE, 23 * CELL_SIZE]
        self.initial_pacman = Image.open("pictures/pm_initial.png")
        self.initial_pm_resized = self.image_initiator("pictures/pm_initial.png")
        self.down_open = self.image_initiator("pictures/pm_down_open.png")
        self.down_closed = self.image_initiator("pictures/pm_down_closed.png")
        self.up_open = self.image_initiator("pictures/pm_up_open.png")
        self.up_closed = self.image_initiator("pictures/pm_up_closed.png")
        self.right_open = self.image_initiator("pictures/pm_right_open.png")
        self.right_closed = self.image_initiator("pictures/pm_right_closed.png")
        self.left_open = self.image_initiator("pictures/pm_left_open.png")
        self.left_closed = self.image_initiator("pictures/pm_left_closed.png")

        self.death_1 = self.image_initiator("pictures/pacman1-removebg-preview.png")
        self.death_2 = self.image_initiator("pictures/pacman2-removebg-preview.png")
        self.death_3 = self.image_initiator("pictures/pacman3-removebg-preview.png")
        self.death_4 = self.image_initiator("pictures/pacman4-removebg-preview.png")
        self.death_5 = self.image_initiator("pictures/pacman5-removebg-preview.png")
        self.death_6 = self.image_initiator("pictures/pacman6-removebg-preview.png")
        self.death_7 = self.image_initiator("pictures/pacman7-removebg-preview.png")
        self.death_8 = self.image_initiator("pictures/pacman8-removebg-preview.png")
        self.death_9 = self.image_initiator("pictures/pacman9-removebg-preview.png")
        self.death_10 = self.image_initiator('pictures/pacman10-removebg-preview.png')

        Window.bind('<Left>', self.move_left)
        Window.bind('<Right>', self.move_right)
        Window.bind('<Up>', self.move_up)
        Window.bind('<Down>', self.move_down)

        self.sprite_dict = self.create_pacman_sprite_dict()
        self.possibility_dict = {"up": self.can_move_up, "down": self.can_move_down,
                                 "right": self.can_move_right, "left": self.can_move_left}
        self.death_sprites_list = self.create_death_sprites_list()

        self.pacman_photo = None
        self.id = self.create_pacman()

        self.is_moving = False
        self.current_move_proces = None
        self.moving_proces_id = None
        self.absolut_stop = False

        self.animation_delay = (DELAY // ANIMATION_STEP)

    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            return True
        return False

    @staticmethod
    def image_initiator(image):
        return ImageTk.PhotoImage(Image.open(image).resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS))

    def create_pacman(self):
        image = self.initial_pacman
        resized_image = image.resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS)
        self.pacman_photo = ImageTk.PhotoImage(resized_image)
        id = self.canvas.create_image(self.canvas_position[0] + CELL_SIZE / 2, self.canvas_position[1] + CELL_SIZE / 2, image=self.pacman_photo)

        return id

    def create_pacman_sprite_dict(self):
        up_dict = {"open": self.up_open, "closed": self.up_closed}
        down_dict = {"open": self.down_open, "closed": self.down_closed}
        left_dict = {"open": self.left_open, "closed": self.left_closed}
        right_dict = {"open": self.right_open, "closed": self.right_closed}

        sprite_dict = {"up": up_dict, "down": down_dict, "left": left_dict, "right": right_dict}

        return sprite_dict

    def create_death_sprites_list(self):
        death_sprites_list = [self.death_1, self.death_2, self.death_3, self.death_4,
                              self.death_5, self.death_6, self.death_7, self.death_8,
                              self.death_9, self.death_10]
        return death_sprites_list

    def move_up(self, event):
        if self.is_moving and self.current_move_proces == "up":
            return
        direction = "up"
        visual_move_coordinates = [0, -ANIMATION_STEP_SIZE]
        self.default_move(direction, visual_move_coordinates)

    def move_down(self, event):
        if self.is_moving and self.current_move_proces == "down":
            return
        direction = "down"
        visual_move_coordinates = [0, ANIMATION_STEP_SIZE]
        self.default_move(direction, visual_move_coordinates)

    def move_right(self, event):
        if self.is_moving and self.current_move_proces == "right":
            return
        direction = "right"
        visual_move_coordinates = [ANIMATION_STEP_SIZE, 0]
        self.default_move(direction, visual_move_coordinates)

    def move_left(self, event):
        if self.is_moving and self.current_move_proces == "left":
            return
        direction = "left"
        visual_move_coordinates = [-ANIMATION_STEP_SIZE, 0]
        self.default_move(direction, visual_move_coordinates)

    def default_move(self, direction, visual_move_coordinates):
        if self.absolut_stop:
            return
        elif self.possibility_dict[direction]():
            self.stop_moving()
            self.is_moving = True
            self.current_move_proces = direction

            self.smooth_move(visual_move_coordinates[0], visual_move_coordinates[1])
            self.moving_proces_id = Window.after(DELAY, lambda: self.default_move(direction, visual_move_coordinates))
        return

    def smooth_move(self, dx, dy, counter=0):
        if counter > 9:
            return

        self.canvas.move(self.id, dx, dy)

        if self.is_even(counter):
            self.canvas.itemconfig(self.id, image=self.sprite_dict[self.current_move_proces]["open"])
        else:
            self.canvas.itemconfig(self.id, image=self.sprite_dict[self.current_move_proces]["closed"])

        counter += 1
        Window.after(self.animation_delay, lambda: self.smooth_move(dx, dy, counter))

    def stop_moving(self):
        if self.moving_proces_id is not None:
            self.canvas.after_cancel(self.moving_proces_id)

    def check_special_positions(self):  # TODO: refactor, refactor, refactor
        if self.position == SPECIAL_POS_1:
            self.canvas.move(self.id, -25 * CELL_SIZE, 0)
            self.position[0], self.position[1] = SPECIAL_POS_2[0], SPECIAL_POS_2[1] + 2
            print(self.position)
        elif self.position == SPECIAL_POS_2:
            self.canvas.move(self.id, 25 * CELL_SIZE, 0)
            self.position[0], self.position[1] = SPECIAL_POS_1[0], SPECIAL_POS_1[1] - 2
            print(self.position)
        return

    def visual_death(self, event):  # TODO: death visualisation, teleportation to start position
        self.stop_moving()
        self.absolut_stop = True
        self.canvas.itemconfig(self.id, image=self.initial_pm_resized)
        self.visualisation_death()

    def visualisation_death(self, counter=0):
        n = len(self.death_sprites_list)
        if counter >= n:
            self.death()
            self.canvas.coords(self.id, self.canvas_position[0] + CELL_SIZE / 2, self.canvas_position[1] + CELL_SIZE / 2)
            self.canvas.itemconfig(self.id, image=self.initial_pm_resized)
            self.absolut_stop = False
            self.position = [23, 13]
            return
        self.canvas.itemconfig(self.id, image=self.death_sprites_list[counter])
        counter += 1
        Window.after(DELAY, lambda: self.visualisation_death(counter))

if __name__ == "__main__":
    m = FieldDrawing(FIELD)
    m.draw_field()
    vp = VisualPacMan()

    Window.bind('<Escape>', vp.visual_death)
    Window.mainloop()