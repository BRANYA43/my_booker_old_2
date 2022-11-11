import wx

from builders.info import BInfo
from funcs_support import test_dialog


class VInfo(BInfo):
    def __init__(self, parent):
        super().__init__(parent)
        self.add_widgets()
        self.build_view()

    def add_widgets(self):
        self.add_static_label('product', 'size')
        self.add_static_label('name_', 'size_', name_label=False)
        self.add_btn('ok')

    def build_view(self):
        border = 10
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        grid_sizer = wx.GridBagSizer(10, 10)
        grid_sizer.Add(self.static_labels['name'], pos=(0, 0), flag=wx.ALIGN_RIGHT)
        grid_sizer.Add(self.static_labels['size'], pos=(1, 0), flag=wx.ALIGN_RIGHT)
        grid_sizer.Add(self.static_labels['name_'], pos=(0, 1))
        grid_sizer.Add(self.static_labels['size_'], pos=(1, 1))
        main_sizer.Add(grid_sizer, flag=wx.ALL, border=border)
        main_sizer.Add(self.btns['ok'], flag=wx.ALIGN_CENTER | wx.TOP, border=20)
        self.SetSizer(main_sizer)


if __name__ == '__main__':
    test_dialog(VInfo)
