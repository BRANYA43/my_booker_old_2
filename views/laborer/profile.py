import wx

import lang.en as lang
from builders.dialog import BDialog
from models.list import MList
from funcs_support import test_dialog


class VProfile(BDialog):
    def __init__(self, parent):
        super().__init__(parent=parent, size=(400, 250))
        self.add_widgets()
        self.build_view()

    def add_widgets(self):
        self.add_static_label('full_name', 'payment', 'rate')
        self.add_entry_field('full_name', value=lang.NAMES['pattern_name'], width=216)
        self.add_entry_field('rate', value='0', width=76)
        self.add_combobox('payment', [lang.NAMES['piecework'], lang.NAMES['hourly_work']], width=216)
        self.add_btn('save')

    def build_view(self):
        border = 10
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        grid_sizer = wx.GridBagSizer(10, 10)
        grid_sizer.Add(self.static_labels['full_name'], pos=(0, 0), flag=wx.ALIGN_RIGHT)
        grid_sizer.Add(self.static_labels['payment'], pos=(1, 0), flag=wx.ALIGN_RIGHT)
        grid_sizer.Add(self.static_labels['rate'], pos=(2, 0), flag=wx.ALIGN_RIGHT)
        grid_sizer.Add(self.entry_fields['full_name'], pos=(0, 1))
        grid_sizer.Add(self.entry_fields['rate'], pos=(2, 1))
        grid_sizer.Add(self.comboboxes['payment'], pos=(1, 1))
        main_sizer.Add(grid_sizer, flag=wx.ALIGN_LEFT | wx.ALL, border=border)
        main_sizer.Add(self.btns['save'], flag=wx.BOTTOM | wx.ALIGN_RIGHT | wx.ALL, border=border)
        self.SetSizer(main_sizer)


if __name__ == '__main__':
    test_dialog(VProfile)
