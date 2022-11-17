from abc import abstractmethod

import wx

from builders.frame import FrameBuilder


class NotebookBuilder(FrameBuilder):
    def __init__(self, parent, title=wx.EmptyString, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        super().__init__(parent=parent, title=title, size=size, style=style)
        self.pages = {}
        self.notebook = wx.Notebook(self)

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

