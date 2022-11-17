from abc import abstractmethod

import wx

from builders.builder import Builder


class BDialog(wx.Dialog, Builder):
    def __init__(self, parent, title=wx.EmptyString, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE):
        wx.Dialog.__init__(self, parent, title=title, size=size, style=style)
        Builder.__init__(self, parent)

    @abstractmethod
    def create_widgets(self):
        pass

    @abstractmethod
    def build_view(self):
        pass


if __name__ == '__main__':
    pass
