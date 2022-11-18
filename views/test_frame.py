import wx


class TestFrame(wx.Frame):
    def __init__(self, window, *attr):
        super().__init__(parent=None, title='TEST-FRAME', size=(800, 600))
        self.window = window(self, *attr)

    def show_frame(self):
        self.Center()
        self.Show()

    def show_dialog(self):
        self.window.Center()
        self.window.ShowModal()


if __name__ == '__main__':
    ...