import wx

from builders.info import BInfo
from funcs_support import test_dialog


class VInfo(BInfo):
    def __init__(self, parent):
        super().__init__(parent)
        self.add_widgets()
        self.build_view()

    def add_widgets(self):
        self.add_static_label('detail', 'count', 'operation', 'cost')
        self.add_static_label('detail_', 'count_', 'operation_', 'cost_', name_label=False)
        self.add_btn('ok')

    def build_view(self):
        border = 10
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        grid_sizer = wx.GridBagSizer(10, 10)
        grid_sizer.Add(self.static_labels['detail'], pos=(0, 0), flag=wx.ALIGN_RIGHT)
        grid_sizer.Add(self.static_labels['count'], pos=(1, 0), flag=wx.ALIGN_RIGHT)
        grid_sizer.Add(self.static_labels['operation'], pos=(2, 0), flag=wx.ALIGN_RIGHT)
        grid_sizer.Add(self.static_labels['cost'], pos=(3, 0), flag=wx.ALIGN_RIGHT)
        grid_sizer.Add(self.static_labels['detail_'], pos=(0, 1))
        grid_sizer.Add(self.static_labels['count_'], pos=(1, 1))
        grid_sizer.Add(self.static_labels['operation_'], pos=(2, 1))
        grid_sizer.Add(self.static_labels['cost_'], pos=(3, 1))
        main_sizer.Add(grid_sizer, flag=wx.ALL, border=border)
        main_sizer.Add(self.btns['ok'], flag=wx.ALIGN_CENTER | wx.TOP, border=20)
        self.SetSizer(main_sizer)


if __name__ == '__main__':
    test_dialog(VInfo)