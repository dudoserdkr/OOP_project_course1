from VisualPacMan import VisualPacMan
from Ghost_logic.GhostDrawer import GhostDrawer
from FieldDrawing import FieldDrawing
from Field import FIELD
from Window import Window
from Ghost_logic.Blinky import Blinky


if __name__ == '__main__':
    m = FieldDrawing(FIELD)
    m.draw_field()
    vp = VisualPacMan()
    b = Blinky()
    b.pacman = vp
    b.condition = b.HUNTING

    drawer = GhostDrawer(b)
    drawer.draw()
    print(vp.position)
    Window.mainloop()
