import wx

import config.config as cfg
import lang.en as lang
from funcs_support import reiterate_func


class Constructor:
    def __init__(self):
        self.btns = {}
        self.comboboxes = {}
        self.static_labels = {}
        self.entry_fields = {}

    @reiterate_func
    def add_btn(self, name: str, width=180):
        key = name
        name = lang.NAMES[name]
        self.btns.setdefault(key, wx.Button(self, label=name, size=(width, -1)))

    def bind_btn(self,  name: str, func):
        button = self.btns[name]
        self.Bind(wx.EVT_BUTTON, func, button)

    @reiterate_func
    def enable_btn(self, name: str):
        self.btns[name].Enable(True)

    @reiterate_func
    def disable_btn(self, name: str):
        self.btns[name].Enable(False)

    def add_combobox(self, name: str, choices: list[str]):
        self.comboboxes.setdefault(name, wx.ComboBox(self, value=choices[0], choices=choices, style=wx.CB_READONLY))

    @reiterate_func
    def add_static_label(self, name: str):
        key = name
        name = lang.NAMES[name] + ':'
        self.static_labels.setdefault(key, wx.StaticText(self, label=name))

    @reiterate_func
    def add_entry_field(self, name: str):
        self.entry_fields.setdefault(name, wx.TextCtrl(self))

    def add_widgets(self):
        raise NotImplemented

    def build_view(self):
        raise NotImplemented


if __name__ == '__main__':
    ...
