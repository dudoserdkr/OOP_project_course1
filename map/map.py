from tkinter import *

from PIL import ImageTk, Image


map = [
 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],  # 0
 [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],  # 1
 [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],  # 2
 [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],  # 3
 [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],  # 4
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],  # 5
 [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],  # 6
 [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],  # 7
 [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],  # 8
 [1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1],  # 9
 [1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1],  # 10
 [1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1],  # 11
 [1,1,1,1,1,1,0,1,1,0,2,2,2,2,2,2,2,2,0,1,1,0,1,1,1,1,1,1],  # 12
 [1,1,1,1,1,1,0,1,1,0,2,2,2,2,2,2,2,2,0,1,1,0,1,1,1,1,1,1],  # 13
 [3,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,3],  # middle 14
 [1,1,1,1,1,1,0,1,1,0,2,2,2,2,2,2,2,2,0,1,1,0,1,1,1,1,1,1],  # 15
 [1,1,1,1,1,1,0,1,1,0,2,2,2,2,2,2,2,2,0,1,1,0,1,1,1,1,1,1],  # 16
 [1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1],  # 17
 [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],  # 18
 [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],  # 19
 [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],  # 20
 [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],  # 21
 [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],  # 22
 [1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],  # 23
 [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],  # 24
 [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],  # 25
 [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],  # 26
 [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],  # 27
 [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],  # 28
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],  # 29
 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],  # 30
]

width = len(map[0])
height = len(map)
cell_size = 20

DELAY = 500

pacman_matrix_position = [23, 13]
pacman_canvas_position = [13 * cell_size, 23*cell_size]

current_pacman_matrix_position = pacman_matrix_position

win = Tk()
win.title("PacMan")
canvas_width = width * cell_size
canvas_height = height * cell_size
win.config(width=canvas_width, height=canvas_height)
win.resizable(False, False)
canvas = Canvas(win, width=canvas_width, height=canvas_height, bg='black')
canvas.pack()

def update_canvas():
    canvas.delete("all")
    for i in range(height):
        for j in range(width):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            if map[i][j] == 1:
                color = "blue"
            elif map[i][j] == 0:
                color = "black"
            elif map[i][j] == 2:
                color = "blue"
            elif map[i][j] == 3:
                color = "pink"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")


# def move_pacman_left(event):  # y ----
#     curr_y, curr_x = current_pacman_matrix_position
#     if map[curr_y][curr_x - 1] == 1 or map[curr_y][curr_x - 1] == 2:
#         return
#     canvas.move(pacman_id, -cell_size, 0)
#     current_pacman_matrix_position[1] -= 1
#
#
# def move_pacman_right(event):  # y ++++
#     curr_y, curr_x = current_pacman_matrix_position
#     if map[curr_y][curr_x + 1] == 1 or map[curr_y][curr_x + 1] == 2:
#         return
#     canvas.move(pacman_id, cell_size, 0)
#     current_pacman_matrix_position[1] += 1
#
#
# def move_pacman_down(event):  # x ++++    curr_y, curr_x = current_pacman_matrix_position
#     curr_y, curr_x = current_pacman_matrix_position
#     if map[curr_y + 1][curr_x] == 1 or map[curr_y + 1][curr_x] == 2:
#         return
#     canvas.move(pacman_id, 0, cell_size)
#     current_pacman_matrix_position[0] += 1
#
#
# def move_pacman_up(event):  # x ----
#     curr_y, curr_x = current_pacman_matrix_position
#     if map[curr_y - 1][curr_x] == 1 or map[curr_y - 1][curr_x] == 2:
#         return
#     canvas.move(pacman_id, 0, -cell_size)
#     current_pacman_matrix_position[0] -= 1

###########

def move_pacman_up(event):  # y ----
    curr_y, curr_x = current_pacman_matrix_position
    if map[curr_y - 1][curr_x] == 1 or map[curr_y - 1][curr_x] == 2:
        return
    canvas.move(pacman_id, 0, -cell_size)
    current_pacman_matrix_position[0] -= 1
    win.after(DELAY , lambda: move_pacman_up(event))


def move_pacman_down(event):  # y ++++
    curr_y, curr_x = current_pacman_matrix_position
    if map[curr_y + 1][curr_x] == 1 or map[curr_y + 1][curr_x] == 2:
        return
    canvas.move(pacman_id, 0, cell_size)
    current_pacman_matrix_position[0] += 1
    win.after(DELAY , lambda: move_pacman_down(event))


def move_pacman_right(event):  # x ++++
    curr_y, curr_x = current_pacman_matrix_position
    if map[curr_y][curr_x + 1] == 1 or map[curr_y][curr_x + 1] == 2:
        return
    canvas.move(pacman_id, cell_size, 0)
    current_pacman_matrix_position[1] += 1
    win.after(DELAY , lambda: move_pacman_right(event))


def move_pacman_left(event):  # x ----
    curr_y, curr_x = current_pacman_matrix_position
    if map[curr_y][curr_x - 1] == 1 or map[curr_y][curr_x - 1] == 2:
        return
    canvas.move(pacman_id, -cell_size, 0)
    current_pacman_matrix_position[1] -= 1
    win.after(DELAY , lambda: move_pacman_left(event))




# def move_pacman(event):
#     if event.keysym == 'Left':
#         canvas.move(pacman_id, -cell_size, 0)
#     elif event.keysym == 'Right':
#         canvas.move(pacman_id, cell_size, 0)
#     elif event.keysym == 'Up':
#         canvas.move(pacman_id, 0, -cell_size)
#     elif event.keysym == 'Down':
#         canvas.move(pacman_id, 0, cell_size)





# def update_canvas_with_pacman(picture):
#     image = picture
#
#     resized_image = image.resize((cell_size, cell_size), Image.Resampling.LANCZOS)
#
#     global pacman_photo
#     pacman_photo = ImageTk.PhotoImage(resized_image)
#
#     canvas.create_image(200, 150, image=pacman_photo)


update_canvas()
picture = Image.open("pictures/PacMan.png")
# update_canvas_with_pacman(picture)
image = picture

resized_image = image.resize((cell_size, cell_size), Image.Resampling.LANCZOS)

pacman_photo = ImageTk.PhotoImage(resized_image)

pacman_id = canvas.create_image(pacman_canvas_position[0] + 10, pacman_canvas_position[1] + 10, image=pacman_photo)


win.bind('<Left>', move_pacman_left)
win.bind('<Right>', move_pacman_right)
win.bind('<Up>', move_pacman_up)
win.bind('<Down>', move_pacman_down)

win.mainloop()
