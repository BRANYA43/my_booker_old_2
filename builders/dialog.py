from abc import abstractmethod

import wx

from builders.builder import Builder


class DialogBuilder(wx.Dialog, Builder):
    def __init__(self, parent, title=wx.EmptyString, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE):
        wx.Dialog.__init__(self, parent, title=title)
        Builder.__init__(self, parent, size=size, style=style)

    @abstractmethod
    def create_widgets(self):
        pass

    @abstractmethod
    def build_view(self):
        pass


if __name__ == '__main__':
    pass
