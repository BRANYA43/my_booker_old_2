import wx

import config.config as cfg


def reiterate_func_with_one_arg(func):
    def wrapper(self, *args, **kwargs):
        for arg in args:
            func(self, arg, **kwargs)
    return wrapper


def reiterate_func_with_two_args(func):
    def wrapper(self, *args, **kwargs):
        for i in range(0, len(args), 2):
            func(self, args[i], args[i+1], **kwargs)
    return wrapper


def reiterate_get_func_with_one_arg(func):

    def wrapper(self, *args, **kwargs):
        if len(args) == 1:
            return func(self, args[0], **kwargs)
        else:
            ret = []
            for arg in args:
                ret.append(func(self, arg, **kwargs))
            return tuple(ret)

    return wrapper


def reiterate_get_func_with_two_args(func):

    def wrapper(self, *args, **kwargs):
        if len(args) == 2:
            return func(self, args[0], args[1], **kwargs)
        else:
            ret = []
            for i in range(0, len(args), 2):
                ret.append(func(self, args[i], args[i + 1], **kwargs))
            return tuple(ret)

    return wrapper





# # Decorate for use class
# def reiterate_func(func):
#     def wrapper(self, *args, **kwargs):
#         for arg in args:
#             func(self, arg, **kwargs)
#     return wrapper
#
#
# def is_selected_object(func):
#     def wrapper(self, *args, **kwargs):
#         if self.model.selected_object is not None:
#             func(self, *args, **kwargs)
#     return wrapper


# testing func
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
