import wx

import config.config as cfg


# Decorate for use class
def reiterate_func(func):
    def wrapper(self, *args, **kwargs):
        for arg in args:
            func(self, arg, **kwargs)
    return wrapper


def is_selected_object(func):
    def wrapper(self, *args, **kwargs):
        if self.model.selected_object is not None:
            func(self, *args, **kwargs)
    return wrapper


def test_panel(panel):
    class TestFrame(wx.Frame):
        def __init__(self):
            super(TestFrame, self).__init__(parent=None, title='TEST-FRAME', size=cfg.SIZE_FRAME)
            self.panel = panel(self)

        def show(self):
            self.Center()
            self.Show()

    app = wx.App()
    test_frame = TestFrame()
    test_frame.show()
    app.MainLoop()


def test_frame(frame):
    app = wx.App()
    test_frame = frame(parent=None)
    test_frame.Center()
    test_frame.Show()
    app.Mainloop()


def test_dialog(dialog):
    app = wx.App()

    class TestFrame(wx.Frame):
        def __init__(self):
            super(TestFrame, self).__init__(parent=None, title='TEST-FRAME', size=cfg.SIZE_FRAME)
            self.dialog = dialog(self)
            self.dialog.ShowModal()
    test_frame = TestFrame()
    test_frame.Center()
    test_frame.Show()
    app.MainLoop()
