import wx

import config.config as cfg
import lang.en as lang
from funcs_support import reiterate_func


class Builder:
    def __init__(self):
        self.btns = {}
        self.comboboxes = {}
        self.static_labels = {}
        self.entry_fields = {}

    @reiterate_func
    def add_btn(self, name: str, width=160):
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

    def add_combobox(self, name: str, choices: list[str], *, width=200, style=wx.CB_READONLY):
        self.comboboxes.setdefault(name, wx.ComboBox(self, value=choices[0], size=(width, -1), choices=choices, style=style))

    def set_value_combobox(self, name: str, value: str):
        self.comboboxes[name].SetValue(value)

    def get_value_combobox(self, name: str) -> str:
        return self.comboboxes[name].GetValue()

    @reiterate_func
    def add_static_label(self, name: str, *, name_label=True):
        key = name
        name = (lang.NAMES[name] + ':') if name_label else 'None'
        self.static_labels.setdefault(key, wx.StaticText(self, label=name))

    def set_label_static_label(self, name: str, label: str):
        self.static_labels[name].SetLabel(label)

    @reiterate_func
    def add_entry_field(self, name: str, *, value=wx.EmptyString, width=200, style=0):
        self.entry_fields.setdefault(name, wx.TextCtrl(self, value=value, size=(width, -1), style=style))

    def set_value_entry_field(self, name: str, value: str):
        self.entry_fields[name].SetValue(value)

    def get_value_entry_field(self, name: str) -> str:
        return self.entry_fields[name].GetValue()

    def add_widgets(self):
        raise NotImplemented

    def build_view(self):
        raise NotImplemented


if __name__ == '__main__':
    ...
