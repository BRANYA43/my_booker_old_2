import wx


class TestFrame(wx.Frame):
    def __init__(self, panel=None, dialog=None, *attrs):
        super().__init__(parent=None, title='TEST-FRAME', size=(800, 600))
        if panel is not None:
            main_sizer = wx.BoxSizer(wx.VERTICAL)
            panel = panel(self, *attrs)
            main_sizer.Add(panel, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
            self.SetSizer(main_sizer)
        elif dialog is not None:
            self.dialog = dialog(self, *attrs)

    def show_frame(self):
        self.Center()
        self.Show()

    def show_dialog(self):
        self.dialog.Center()
        self.dialog.ShowModal()


if __name__ == '__main__':
    ...
