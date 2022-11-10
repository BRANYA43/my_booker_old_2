import wx

from builders.dialog import BDialog
from funcs_support import test_dialog


class BInfo(BDialog):
    def __init__(self, parent, title=wx.EmptyString, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE):
        super().__init__(parent, title=title, size=size, style=style)

    def set_info(self, **items):
        for key, item in items.items():
            self.set_label_static_label(key + '_', item)
