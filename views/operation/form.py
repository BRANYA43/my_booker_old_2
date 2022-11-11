import wx

from builders.dialog import BDialog
from funcs_support import test_dialog


class VForm(BDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.add_widgets()
        self.build_view()

    def add_widgets(self):
        self.add_static_label('operation', 'cost')
        self.add_entry_field('operation', 'cost')
        self.add_btn('save')

    def build_view(self):
        border = 10
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        grid_size = wx.GridBagSizer(10, 10)
        grid_size.Add(self.static_labels['operation'], pos=(0, 0), flag=wx.ALIGN_RIGHT)
        grid_size.Add(self.static_labels['cost'], pos=(1, 0), flag=wx.ALIGN_RIGHT)
        grid_size.Add(self.entry_fields['operation'], pos=(0, 1))
        grid_size.Add(self.entry_fields['cost'], pos=(1, 1))
        main_sizer.Add(grid_size, flag=wx.ALL, border=border)
        main_sizer.Add(self.btns['save'], flag=wx.ALIGN_RIGHT | wx.RIGHT | wx.TOP, border=10)
        self.SetSizer(main_sizer)


if __name__ == '__main__':
    test_dialog(VForm)