from abc import abstractmethod

import wx

from builders.frame import FrameBuilder


class NotebookBuilder(FrameBuilder):
    def __init__(self, parent, id_=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE,
                 name=wx.FrameNameStr):
        super().__init__(parent, id_, title, pos, size, style, name)
        self.pages = {}
        self.notebook = wx.Notebook(self)
        self.main_sizer.Add(self.notebook, proportion=1, flag=wx.EXPAND)

    @abstractmethod
    def create_widgets(self):
        pass

    @abstractmethod
    def build_view(self):
        pass

    def add_page(self, name: str, panel):
        n = len(self.pages)
        self.pages.setdefault(name, panel)
        self.notebook.InsertPage(n, self.pages[name], name)

