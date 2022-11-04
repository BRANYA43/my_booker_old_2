import wx

import config.config as cfg
import lang.en as lang


class Constructor(wx.Frame, wx.Panel, wx.Dialog):
    __FRAME = 0
    __PANEL = 1
    __DIALOG = 2

    def __init__(self, window=0, parent=None, size=wx.DefaultSize, title=wx.EmptyString):
        if window == self.__PANEL:
            wx.Panel.__init__(self, parent=parent, size=size)
        elif window == self.__DIALOG:
            wx.Dialog.__init__(self, parent=parent, title=title, size=size)
        else:
            wx.Frame.__init__(self, parent=parent, title=title, size=size)

        self.widgets = {}

    # btn funcs
    def add_btn(self, name: str):
        self.__add_new_dict('btns')
        key = name
        name = lang.NAMES[name]
        self.widgets['btns'].setdefault(key, wx.Button(self, label=name))

    def bind_btn(self, func, name: str):
        button = self.widgets['btns'][name]
        self.Bind(wx.EVT_BUTTON, func, button)

    def enable_btn(self, name: str):
        self.widgets['btns'][name].Enable(True)

    def disable_btn(self, name: str):
        self.widgets['btns'][name].Enable(False)

    # widgets funcs
    def add_combobox(self, name: str, choices: list[str]):
        self.__add_new_dict('comboboxes')
        self.widgets['comboboxes'].setdefault(name, wx.ComboBox(self, value=choices[0], choices=choices, style=wx.CB_READONLY))

    def add_static_text(self, label: str):
        self.__add_new_dict('static_texts')
        key = label
        label = lang.NAMES[label] + ':'
        self.widgets['static_texts'].setdefault(key, wx.StaticText(self, label=label))

    def add_entry_field(self, name: str):
        self.__add_new_dict('entry_fields')
        self.widgets['entry_fields'].setdefault(name, wx.TextCtrl(self))

    def build_view(self):
        raise NotImplemented

    def __add_new_dict(self, dict_widgets: str):
        if self.__is_this_dict_in_widgets(dict_widgets):
            self.widgets.setdefault(dict_widgets, {})

    def __is_this_dict_in_widgets(self, dict_widgets: str) -> bool:
        if self.widgets.get(dict_widgets) is not None:
            return True
        return False
