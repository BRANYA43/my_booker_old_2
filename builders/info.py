from abc import abstractmethod

import wx

from builders.dialog import DialogBuilder
from support_tools.funcs import reiterate_func_with_one_arg


class InfoBuilder(DialogBuilder):
    def __init__(self, parent, title=wx.EmptyString, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE):
        super(InfoBuilder, self).__init__(parent, title=title, size=size, style=style)
        self.labels = []

    @abstractmethod
    def create_widgets(self):
        pass

    @abstractmethod
    def build_view(self):
        pass

    @reiterate_func_with_one_arg
    def create_static_text(self, name: str, *, add=False, auto_name_label=False, colon=False, label='Not named', pos=wx.DefaultPosition, width=-1, height=-1, style=0):
        super().create_static_text(name, auto_name_label=auto_name_label, colon=colon, label=label, pos=pos, width=width, height=height, style=style)
        if add:
            self.labels.append(name)

    def set_labels(self, *values: str):
        for label, value in zip(self.labels, values):
            self.get_static_text(label).SetLabel(value)


if __name__ == '__main__':
    ...
