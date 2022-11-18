from abc import abstractmethod

import wx

import config.config as cfg
from builders.builder import Builder


class PanelBuilder(wx.Panel, Builder):
    def __init__(self, parent, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL):
        wx.Panel.__init__(self, parent)
        Builder.__init__(self, parent, size=size, style=style)

    @abstractmethod
    def create_widgets(self):
        pass

    @abstractmethod
    def build_view(self):
        pass


if __name__ == '__main__':
    ...
