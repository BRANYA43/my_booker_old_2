import wx

import lang.en as lang
from builders.dialog import BDialog
from funcs_support import test_dialog


class VInfo(BDialog):
    def __init__(self, parent):
        super().__init__(parent=parent, size=(380, 240))
        self.add_widgets()
        self.build_view()

    def add_widgets(self):
        self.add_static_label('full_name', 'payment', 'rate')
        self.add_static_label('full_name_', 'payment_', 'rate_', name_label=False)
        self.add_btn('ok')

    def build_view(self):
        border = 10
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        grid_sizer = wx.GridBagSizer(10, 10)
        grid_sizer.Add(self.static_labels['full_name'], pos=(0, 0), flag=wx.ALIGN_RIGHT)
        grid_sizer.Add(self.static_labels['payment'], pos=(1, 0), flag=wx.ALIGN_RIGHT)
        grid_sizer.Add(self.static_labels['rate'], pos=(2, 0), flag=wx.ALIGN_RIGHT)
        grid_sizer.Add(self.static_labels['full_name_'], pos=(0, 1))
        grid_sizer.Add(self.static_labels['payment_'], pos=(1, 1))
        grid_sizer.Add(self.static_labels['rate_'], pos=(2, 1))
        main_sizer.Add(grid_sizer, flag=wx.ALL, border=border)
        main_sizer.Add(self.btns['ok'], flag= wx.ALIGN_CENTER | wx.TOP, border=20)
        self.SetSizer(main_sizer)

    def set_info(self, full_name: str, payment: str, rate: str):
        self.set_label_static_label('full_name_', full_name)
        self.set_label_static_label('payment_', payment)
        self.set_label_static_label('rate_', rate)



if __name__ == '__main__':
    test_dialog(VInfo)