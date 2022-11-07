import wx

import config.config as cfg
from constructors.constructor import Constructor


class PanelConstructor(wx.Panel, Constructor):
    def __init__(self, parent, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL):
        wx.Panel.__init__(self, parent, size=size, style=style)
        Constructor.__init__(self)
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetPointSize(cfg.SIZE_FONT)
        self.SetFont(font)


if __name__ == '__main__':
    ...
