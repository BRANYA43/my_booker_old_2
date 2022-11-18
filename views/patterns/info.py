from abc import abstractmethod

import wx

import lang.en as lang
from builders.info import InfoBuilder
from support_tools.funcs import test_dialog


class InfoPattern(InfoBuilder):
    def __init__(self, parent, title=wx.EmptyString, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE):
        super().__init__(parent, title=title, size=size, style=style)

    @abstractmethod
    def create_widgets(self):
        self.create_btn(lang.OK, auto_name_label=True)

    @abstractmethod
    def build_view(self):
        self.main_sizer.Add(self.get_btn(lang.OK), flag=wx.ALIGN_CENTER | wx.TOP, border=40)


if __name__ == '__main__':
    class InfoView(InfoPattern):
        def __init__(self, parent):
            super().__init__(parent)
            self.create_widgets()
            self.build_view()

        def create_widgets(self):
            super().create_widgets()

        def build_view(self):
            super().build_view()
    test_dialog(InfoView)
