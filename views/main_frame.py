import wx

import lang.en as lang
from builders.notebook import NotebookBuilder
from views.laborer.list import VList
from models.list import MList
from controllers.list_laborer import CLaborerList


class MainFrame(NotebookBuilder):
    def __init__(self):
        super().__init__(parent=None, size=(800, 600))
        self.build_tab_laborer()

    def create_widgets(self):
        pass

    def build_view(self):
        pass

    def build_tab_laborer(self):
        model = MList()
        list_view = VList(self.notebook)
        controller = CLaborerList(model, list_view)
        self.add_page(lang.NAMES['laborers'], list_view)

    def show_frame(self):
        self.Center()
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    main_frame = MainFrame()
    main_frame.show_frame()
    app.MainLoop()
