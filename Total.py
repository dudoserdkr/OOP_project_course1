from Coin import Coin
from Tablet import Tablet
from tkinter import *
from PIL import ImageTk, Image
from VisualPacMan import VisualPacMan
from Canvas import CANVAS
from Window import Window
from Field import FIELD
from FieldDrawing import FieldDrawing
from Canvas import CANVAS
from Score import Score



DELAY = 30

def coin_check(pacman, coin_list):
    #print(f"Pacman {pacman.position}")
    for coin in coin_list:
        coin.change_status(pacman)

    Window.after(DELAY // 30, lambda: coin_check(pacman, coin_list))

def tablet_check(pacman, tablet_list):
    #print(f"Pacman {pacman.position}")
    for tablet in tablet_list:
        tablet.change_status(pacman)

    Window.after(DELAY // 30, lambda: tablet_check(pacman, tablet_list))






if __name__ == "__main__":
    m = FieldDrawing(FIELD)
    m.draw_field()

    ex = []
    for i in range(0, 28):
        for e in range(0, 30):
            c = Coin([i, e])  # СПИСОК
            if FIELD[e][i] == 0 and not (20 > e > 8 and 21 > i > 6) and not (i == 1 and e == 3) and not (i == 1 and e == 23) and not (i == 26 and e == 3) and not (i == 26 and e == 23):
                #c.draw()
                ex.append(c)
    nex = []
    for t in ex:
        t.draw()

    first_tablet = Tablet([1, 3])
    nex.append(first_tablet)
    second_tablet = Tablet([1, 23])
    nex.append(second_tablet)
    third_tablet = Tablet([26, 3])
    nex.append(third_tablet)
    fourth_tablet = Tablet([26, 23])
    nex.append(fourth_tablet)

    first_tablet.draw()
    second_tablet.draw()
    third_tablet.draw()
    fourth_tablet.draw()


    score = Score()
    first_tablet.register_observer(score)
    second_tablet.register_observer(score)
    third_tablet.register_observer(score)
    fourth_tablet.register_observer(score)

    vp = VisualPacMan()
    coin_check(vp, ex)
    tablet_check(vp, nex)





    Window.bind('<Left>', vp.move_left)
    Window.bind('<Right>', vp.move_right)
    Window.bind('<Up>', vp.move_up)
    Window.bind('<Down>', vp.move_down)
    Window.mainloop()