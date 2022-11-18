import wx

import lang.en as lang
from views.patterns.info import InfoPattern
from support_tools.funcs import test_dialog


class InfoView(InfoPattern):
    def __init__(self, parent):
        super().__init__(parent=parent, title=lang.LABORER, size=(400, 230))
        print(self.GetSize())
        self.create_widgets()
        self.build_view()

    def create_widgets(self):
        self.create_static_text(lang.FULL_NAME, lang.PAYMENT, lang.RATE, auto_name_label=True, colon=True)
        self.create_static_text('full_name_', 'payment_', 'rate_', add=True)
        super().create_widgets()

    def build_view(self):
        border = 10
        grid_sizer = wx.GridBagSizer(10, 10)
        grid_sizer.Add(self.get_static_text(lang.FULL_NAME), pos=(0, 0), flag=wx.ALIGN_RIGHT)
        grid_sizer.Add(self.get_static_text(lang.PAYMENT), pos=(1, 0), flag=wx.ALIGN_RIGHT)
        grid_sizer.Add(self.get_static_text(lang.RATE), pos=(2, 0), flag=wx.ALIGN_RIGHT)
        grid_sizer.Add(self.get_static_text('full_name_'), pos=(0, 1))
        grid_sizer.Add(self.get_static_text('payment_'), pos=(1, 1))
        grid_sizer.Add(self.get_static_text('rate_'), pos=(2, 1))
        self.main_sizer.Add(grid_sizer, flag=wx.ALL, border=border)
        super().build_view()


if __name__ == '__main__':
    test_dialog(InfoView)
