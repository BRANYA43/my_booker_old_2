import wx

import config.config as cfg
from constructors.constructor import Constructor


class DialogConstructor(wx.Dialog, Constructor):
    def __init__(self, parent, title=wx.EmptyString, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE):
        wx.Dialog.__init__(self, parent, title=title, size=size, style=style)
        Constructor.__init__(self)
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetPointSize(cfg.SIZE_FONT)
        self.SetFont(font)


if __name__ == '__main__':
    pass
