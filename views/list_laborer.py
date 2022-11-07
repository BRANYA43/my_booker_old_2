import wx

from constructors.list_constructor import ListConstructor
from funcs_support import test_panel


class ListLaborer(ListConstructor):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.add_widgets()
        self.build_view()

    def add_widgets(self):
        self.add_column('laborer', 'id')
        self.set_width_column('laborer', width=200)
        self.hide_column('id')
        self.add_btn('info', 'add', 'edit', 'delete')

    def build_view(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.list_ctrl, flag=wx.ALIGN_CENTRE, border=10)
        btn_sizer = wx.BoxSizer(wx.VERTICAL)
        btn_sizer.Add(self.btns['info'])
        btn_sizer.Add(self.btns['add'])
        btn_sizer.Add(self.btns['edit'])
        btn_sizer.Add(self.btns['delete'])
        main_sizer.Add(btn_sizer, flag=wx.ALIGN_CENTER, border=10)
        self.SetSizer(main_sizer)


if __name__ == '__main__':
    test_panel(ListLaborer)
