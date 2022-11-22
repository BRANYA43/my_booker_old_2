from abc import abstractmethod

import wx

from builders.builder import Builder


class MetaDialogBuilder(type(wx.Dialog), type(Builder)):
    pass


class DialogBuilder(wx.Dialog, Builder, metaclass=MetaDialogBuilder):
    def __init__(self, parent, id_=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE,
                 name=wx.DialogNameStr):
        wx.Dialog.__init__(self, parent, id_, title, pos, size, style, name)
        Builder.__init__(self)

    @abstractmethod
    def create_widgets(self):
        pass

    @abstractmethod
    def build_view(self):
        pass


if __name__ == '__main__':
    pass
