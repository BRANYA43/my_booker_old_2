from abc import abstractmethod

import wx

import config.config as cfg
from builders.builder import Builder


class MetaPanelBuilder(type(wx.Panel), type(Builder)):
    pass


class PanelBuilder(wx.Panel, Builder, metaclass=MetaPanelBuilder):
    def __init__(self, parent, id_=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
        wx.Panel.__init__(self, parent, id_, pos, size, style, name)
        Builder.__init__(self)

    @abstractmethod
    def create_widgets(self):
        pass

    @abstractmethod
    def build_view(self):
        pass


if __name__ == '__main__':
    ...
