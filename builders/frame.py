from abc import abstractmethod

import wx

from builders.builder import Builder


class BFrame(wx.Frame, Builder):
    def __init__(self, parent, title=wx.EmptyString, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, title=title, size=size, style=style)
        Builder.__init__(self, parent)

    @abstractmethod
    def create_widgets(self):
        pass

    @abstractmethod
    def build_view(self):
        pass

if __name__ == '__main__':
    pass
