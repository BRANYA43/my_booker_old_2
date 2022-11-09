import wx

from builders.list import BList
from funcs_support import test_panel


class VList(BList):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.add_widgets()
        self.build_view()

    def add_widgets(self):
        self.set_size_list(240, 330)
        self.add_column('laborer', 'id')
        self.set_width_column('laborer', width=240)
        self.hide_column('id')
        self.add_btn('info', 'add', 'edit', 'delete')

    def build_view(self):
        border = 10
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.list_ctrl, flag=wx.ALIGN_CENTRE | wx.TOP, border=border)
        btn_sizer = wx.BoxSizer(wx.VERTICAL)
        btn_sizer.Add(self.btns['info'], flag=wx.TOP | wx.BOTTOM, border=border)
        btn_sizer.Add(self.btns['add'], flag=wx.BOTTOM, border=border)
        btn_sizer.Add(self.btns['edit'], flag=wx.BOTTOM, border=border)
        btn_sizer.Add(self.btns['delete'])
        main_sizer.Add(btn_sizer, flag=wx.ALIGN_CENTER, border=border)
        self.SetSizer(main_sizer)


if __name__ == '__main__':
    test_panel(VList)
