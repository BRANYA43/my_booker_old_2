from abc import abstractmethod

import wx

from builders.builder import Builder


class MetaFrameBuilder(type(wx.Frame), type(Builder)):
    pass


class FrameBuilder(wx.Frame, Builder, metaclass=MetaFrameBuilder):
    def __init__(self, parent, id_=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE,
                 name=wx.FrameNameStr):
        wx.Frame.__init__(self, parent, id_, title, pos, size, style, name)
        Builder.__init__(self)

    @abstractmethod
    def create_widgets(self):
        pass

    @abstractmethod
    def build_view(self):
        pass


if __name__ == '__main__':
    pass
