from tkinter import Frame,Label,CENTER

import Logics
import constants as c 


class Game2048(Frame):
    def __init__(self):

        self.grid()
        self.title('2048')
        self.master.bind("<Key>",self.key_down)
        self.commands = {c.KEY_UP:Logics.move_up, c.KEY_DOWN : Logics.move_down,
                         c.KEY_LEFT: Logics.move_left , c.KEY_RIGHT : Logics.move_right
                        }

        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
         