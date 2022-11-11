import wx

from builders.panel import BPanel
from funcs_support import test_panel


class VForm(BPanel):
    def __init__(self, parent):
        super().__init__(parent)
        self.add_widgets()
        self.build_view()

    def add_widgets(self):
        self.add_static_label('product', 'size')
        self.add_static_label('table', name_label=False)
        self.set_label_static_label('table', 'TABLE')
        self.add_entry_field('product', 'size')
        self.add_btn('save')

    def build_view(self):
        border = 10
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        grid_sizer = wx.GridBagSizer(10, 10)
        grid_sizer.Add(self.static_labels['product'], pos=(0, 0), flag=wx.ALIGN_RIGHT)
        grid_sizer.Add(self.static_labels['size'], pos=(1, 0), flag=wx.ALIGN_RIGHT)
        grid_sizer.Add(self.entry_fields['product'], pos=(0, 1))
        grid_sizer.Add(self.entry_fields['size'], pos=(1, 1))
        main_sizer.Add(grid_sizer, flag=wx.ALL, border=border)
        main_sizer.Add(self.static_labels['table'], flag=wx.ALIGN_CENTER | wx.ALL, border=border)
        main_sizer.Add(self.btns['save'], flag=wx.ALIGN_RIGHT | wx.TOP | wx.RIGHT, border=border)
        self.SetSizer(main_sizer)


if __name__ == '__main__':
    test_panel(VForm)