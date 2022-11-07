import wx

from constructors.constructor import Constructor


class FrameConstructor(wx.Frame, Constructor):
    def __init__(self, parent, title=wx.EmptyString, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE):
        wx.Frame.__init__(self, parent, title=title, size=size, style=style)
        Constructor.__init__(self)


if __name__ == '__main__':
    pass
