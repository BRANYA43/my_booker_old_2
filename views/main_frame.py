import wx

import config.config as cfg
from views.constructor import Constructor


class MainFrame(Constructor):
    def __init__(self):
        super().__init__(window=0, parent=None, title=cfg.TITLE, size=cfg.SIZE_FRAME)
        notebook = wx.Notebook(self)
        tab_test_0 = wx.Panel(notebook)
        tab_test_1 = wx.Panel(notebook)
        notebook.InsertPage(0, tab_test_0, 'Home')
        notebook.InsertPage(1, tab_test_1, 'Setting')

    def show_frame(self):
        self.Center()
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    main_frame = MainFrame()
    main_frame.show_frame()
    app.MainLoop()
