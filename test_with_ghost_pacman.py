from VisualPacMan import VisualPacMan
from Ghost_logic.GhostDrawer import GhostDrawer
from FieldDrawing import FieldDrawing
from Field import FIELD
from Window import Window
from Ghost_logic.Blinky import Blinky
from Ghost_logic.Pinky import Pinky
from Ghost_logic.Inky import Inky
from Ghost_logic.Clyde import Clyde


if __name__ == '__main__':
    m = FieldDrawing(FIELD)
    m.draw_field()
    vp = VisualPacMan()
    b = Blinky()
    p = Pinky()
    i = Inky()
    c = Clyde()
    b.set_pacman_position(vp.position)
    p.set_pacman_position(vp.position)
    p.set_pacman_direction(vp.direction)
    i.set_pacman_direction(vp.direction)
    i.set_blinky_position(b.position)
    i.set_pacman_position(vp.position)
    c.set_pacman_position(vp.position)
    b.condition = b.HUNTING
    p.condition = p.HUNTING
    i.condition = i.HUNTING
    c.condition = c.HUNTING




    drawer = GhostDrawer(b)
    drawer1 = GhostDrawer(p)
    drawer2 = GhostDrawer(i)
    drawer3 = GhostDrawer(c)
    drawer.draw()
    drawer1.draw()
    drawer2.draw()
    drawer3.draw()
    Window.mainloop()
