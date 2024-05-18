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
        self.down_open = ImageTk.PhotoImage(Image.open("pictures/pm_down_open.png").resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS))
        self.down_closed = ImageTk.PhotoImage(Image.open("pictures/pm_down_closed.png").resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS))
        self.up_open = ImageTk.PhotoImage(Image.open("pictures/pm_up_open.png").resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS))
        self.up_closed = ImageTk.PhotoImage(Image.open("pictures/pm_up_closed.png").resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS))
        self.right_open = ImageTk.PhotoImage(Image.open("pictures/pm_right_open.png").resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS))
        self.right_closed = ImageTk.PhotoImage(Image.open("pictures/pm_right_closed.png").resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS))
        self.left_open = ImageTk.PhotoImage(Image.open("pictures/pm_left_open.png").resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS))
        self.left_closed = ImageTk.PhotoImage(Image.open("pictures/pm_left_closed.png").resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS))

        self.sprite_dict = self.create_pacman_sprite_dict()

        self.pacman_photo = None
        self.id = self.create_pacman()

        self.is_moving = False
        self.current_move_proces = None
        self.moving_proces_id = None

        self.animation_delay = (DELAY // ANIMATION_STEP)

    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            return True
        return False

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

    def move_up(self, event,  skip_first_if=False):
        if self.is_moving and self.current_move_proces == "up" and not skip_first_if:
            return
        if self.can_move_up():
            self.stop_moving()
            self.is_moving = True
            self.current_move_proces = "up"
            self.canvas.itemconfig(self.id, image=self.up_open)

            self.smooth_move(dx=0, dy=-ANIMATION_STEP_SIZE)
            self.moving_proces_id = Window.after(DELAY, lambda: self.move_up(event, True))
        return

    def move_down(self, event, skip_first_if=False):
        if self.is_moving and self.current_move_proces == "down" and not skip_first_if:
            return
        if self.can_move_down():
            self.stop_moving()
            self.is_moving = True
            self.current_move_proces = "down"
            self.canvas.itemconfig(self.id, image=self.down_open)

            self.smooth_move(dx=0, dy=ANIMATION_STEP_SIZE)
            self.moving_proces_id = Window.after(DELAY, lambda: self.move_down(event, True))
        return

    def move_right(self, event, skip_first_if=False):
        if self.is_moving and self.current_move_proces == "right" and not skip_first_if:
            return
        if self.can_move_right():
            self.stop_moving()
            self.is_moving = True
            self.current_move_proces = "right"
            self.canvas.itemconfig(self.id, image=self.right_open)

            self.smooth_move(dx=ANIMATION_STEP_SIZE, dy=0)
            self.check_special_positions()
            self.moving_proces_id = Window.after(DELAY, lambda: self.move_right(event, True))
        return

    def move_left(self, event, skip_first_if=False):
        if self.is_moving and self.current_move_proces == "left" and not skip_first_if:
            return
        if self.can_move_left():
            self.stop_moving()
            self.is_moving = True
            self.current_move_proces = "left"
            self.canvas.itemconfig(self.id, image=self.left_open)

            self.check_special_positions()
            self.smooth_move(dx=-ANIMATION_STEP_SIZE, dy=0)
            self.moving_proces_id = Window.after(DELAY, lambda: self.move_left(event, True))  # TODO: DELAY / self.speed
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

        # self.current_move_proces = None


if __name__ == "__main__":
    m = FieldDrawing(FIELD)
    m.draw_field()
    vp = VisualPacMan()
    Window.bind('<Left>', vp.move_left)
    Window.bind('<Right>', vp.move_right)
    Window.bind('<Up>', vp.move_up)
    Window.bind('<Down>', vp.move_down)
    Window.bind('<Escape>', vp.visual_death)
    Window.mainloop()