import wx

import config.config as cfg
import lang.en as lang


class FormDialog(wx.Dialog):
    def __init__(self, parent, size=cfg.SIZE_DIALOG):
        super().__init__(parent=parent, size=size)
        self.static_texts = {}
        self.widgets = {}
        self.btns = {}
        self.build_dialog()

    def add_static_text(self, *labels):
        for label in labels:
            label_key = label
            label = lang.NAMES[label] + ':'
            self.static_texts.setdefault(label_key, wx.StaticText(self, label=label))

    def add_combobox(self, **keys_and_lists):
        for label, choices in keys_and_lists.items():
            self.widgets.setdefault(label, wx.ComboBox(self, value=choices[0], choices=choices, style=wx.CB_READONLY))

    def add_entry_field(self, *labels):
        for label in labels:
            self.widgets.setdefault(label, wx.TextCtrl(self))

    def add_button(self, *labels):
        for label in labels:
            label_key = label
            label = lang.NAMES[label]
            self.btns.setdefault(label_key, wx.Button(self, label=label))

    def enable_button(self, *labels):
        for label in labels:
            self.btns[label].Enable(True)

    def disable_button(self, *labels):
        for label in labels:
            self.btns[label].Enable(False)

    def bind_button(self, func, label):
        button = self.btns[label]
        self.Bind(wx.EVT_BUTTON, func, button)

    def build_dialog(self):
        raise NotImplemented
