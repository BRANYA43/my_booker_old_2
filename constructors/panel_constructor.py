import wx

from constructors.constructor import Constructor


class PanelConstructor(wx.Panel, Constructor):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL)
        Constructor.__init__(self)


if __name__ == '__main__':
    ...
