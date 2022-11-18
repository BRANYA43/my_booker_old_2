import wx

from builders.list import ListBuilder
from support_tools.funcs import test_panel


class ListView(ListBuilder):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.create_widgets()
        self.build_view()

    def create_widgets(self):
        self.set_size_list(240, 330)
        self.add_column('laborer', 'id')
        self.set_width_column('laborer', 240)
        self.hide_column('id')
        self.create_btn('info', 'add', 'edit', 'delete', auto_name_label=True)

    def build_view(self):
        border = 10
        self.main_sizer.Add(self.list_ctrl, flag=wx.ALIGN_CENTRE | wx.TOP, border=border)
        btn_sizer = wx.BoxSizer(wx.VERTICAL)
        for btn in self.get_btn('info', 'add', 'edit', 'delete'):
            btn_sizer.Add(btn, flag=wx.BOTTOM, border=border)
        self.main_sizer.Add(btn_sizer, flag=wx.ALIGN_CENTER | wx.TOP, border=border)


if __name__ == '__main__':
    test_panel(ListView)
