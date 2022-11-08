import wx

import lang.en as lang
from constructors.dialog_constructor import DialogConstructor
from models.list_ctrl_model import ListCtrlModel
from funcs_support import test_dialog


class ProfileLaborer(DialogConstructor):
    def __init__(self, parent, model: ListCtrlModel):
        super(ProfileLaborer, self).__init__(parent=parent, size=(400, 250))
        self.model = model
        self.add_widgets()
        self.build_view()

    def add_widgets(self):
        self.add_static_label('full_name', 'payment', 'rate')
        self.add_entry_field('full_name', value='01234567890123456789', width=216)
        self.add_entry_field('rate', value='00000$', width=76)
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
        main_sizer.Add(self.btns['save'], flag=wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL, border=border)
        self.SetSizer(main_sizer)


if __name__ == '__main__':
    test_dialog(ProfileLaborer)
