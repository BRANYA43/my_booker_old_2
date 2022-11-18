import wx

import lang.en as lang
from builders.dialog import DialogBuilder
from support_tools.funcs import test_dialog


class ProfileView(DialogBuilder):
    def __init__(self, parent):
        super().__init__(parent=parent, size=(400, 250))
        self.create_widgets()
        self.build_view()

    def create_widgets(self):
        self.create_static_text(lang.FULL_NAME, lang.PAYMENT, lang.RATE, auto_name_label=True, colon=True)
        self.create_text_ctrl('full_name', value=lang.PATTERN_NAME, width=216)
        self.create_text_ctrl('rate', value='0', width=76)
        self.create_combobox('payment', [lang.PIECEWORK, lang.HOURLY_WORK], width=216)
        self.create_btn(lang.SAVE, auto_name_label=True)

    def build_view(self):
        border = 10
        grid_sizer = wx.GridBagSizer(10, 10)
        for i, static_text in enumerate(self.get_static_text(lang.FULL_NAME, lang.PAYMENT, lang.RATE)):
            grid_sizer.Add(static_text, pos=(i, 0), flag=wx.ALIGN_RIGHT)
        full_name, rate = self.get_text_ctrl('full_name', 'rate')
        grid_sizer.Add(full_name, pos=(0, 1))
        grid_sizer.Add(self.get_combobox('payment'), pos=(1, 1))
        grid_sizer.Add(rate, pos=(2, 1))
        self.main_sizer.Add(grid_sizer, flag=wx.ALIGN_LEFT | wx.ALL, border=border)
        self.main_sizer.Add(self.get_btn(lang.SAVE), flag=wx.TOP | wx.ALIGN_CENTER, border=40)


if __name__ == '__main__':
    test_dialog(ProfileView)
