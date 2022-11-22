import wx

from views.test_frame import TestFrame


def test_panel(panel, *attrs):
    app = wx.App()
    test_frame_ = TestFrame(panel=panel, *attrs)
    test_frame_.show_frame()
    app.MainLoop()


def test_frame(frame):
    app = wx.App()
    test_frame_ = frame(parent=None)
    test_frame_.Center()
    test_frame_.Show()
    app.MainLoop()


def test_dialog(dialog, *attrs):
    app = wx.App()
    test_frame_ = TestFrame(dialog=dialog, *attrs)
    test_frame_.show_frame()
    test_frame_.show_dialog()
    app.MainLoop()
