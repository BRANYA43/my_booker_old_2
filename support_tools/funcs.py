import wx

from views.test_frame import TestFrame


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
