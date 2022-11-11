import wx

import lang.en as lang
from builders.notebook import BNotebook
from views.laborer.list import VList
from models.list import MList
from controllers.list_laborer import CLaborerList


class MainFrame(BNotebook):
    def __init__(self):
        super().__init__(parent=None, size=(800, 600))
        self.build_tab_laborer()

    def build_tab_laborer(self):
        controller_laborer = CLaborerList(self.notebook)
        self.add_page(lang.NAMES['laborers'], controller_laborer.list_view)

    def show_frame(self):
        self.Center()
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    main_frame = MainFrame()
    main_frame.show_frame()
    app.MainLoop()
