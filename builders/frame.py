import wx

import config.config as cfg
from builders.builder import Builder


class BFrame(wx.Frame, Builder):
    def __init__(self, parent, title=wx.EmptyString, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, title=title, size=size, style=style)
        Builder.__init__(self)
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetPointSize(cfg.SIZE_FONT)
        self.SetFont(font)

if __name__ == '__main__':
    pass
