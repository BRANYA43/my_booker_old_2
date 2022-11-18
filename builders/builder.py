from abc import ABC, abstractmethod

import wx

import config.config as cfg
from support_tools.funcs import reiterate_func_with_one_arg, reiterate_func_with_two_args, reiterate_get_func_with_two_args, \
    reiterate_get_func_with_one_arg


class MBuilder(type(wx.Window), type(ABC)):
    pass


class Builder(wx.Window, ABC, metaclass=MBuilder):
    NOT_NAMED = 'Not named'
    widget_classes = {
        'btn': wx.Button,
        'static_text': wx.StaticText,
        'text_ctrl': wx.TextCtrl,
        'combobox': wx.ComboBox,
    }

    def __init__(self, parent, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
        ABC.__init__(self)
        wx.Window.__init__(self, parent, pos=pos, size=size, style=style)
        # self.font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        self.font = wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.set_font_size(cfg.FONT_SIZE)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.widgets = {}
        self.SetSizer(self.main_sizer)

    @abstractmethod
    def create_widgets(self):
        pass

    @abstractmethod
    def build_view(self):
        pass

    def set_font_size(self, size: int):
        self.font.SetPointSize(size)
        self.SetFont(self.font)

    def set_font(self, font: wx.Font):
        self.font = font
        self.SetFont(self.font)

    def add_widget(self, type_: str, name: str, widget):
        if self.widgets.get(type_) is None:
            self.widgets.setdefault(type_, {})
        if self.widgets[type_].get(name) is not None:
            raise Exception
        self.widgets[type_].setdefault(name, widget)

    def create_widget(self, type_: str, name: str, **kwargs):
        widget = self.widget_classes[type_](self, **kwargs)
        self.add_widget(type_, name, widget)

    @reiterate_get_func_with_two_args
    def get_widget(self, type_: str, name: str) -> wx.Button | wx.StaticText | wx.TextCtrl | wx.ComboBox | tuple[
                                                   wx.Button | wx.StaticText | wx.TextCtrl | wx.ComboBox]:
        return self.widgets[type_][name]

    @reiterate_func_with_two_args
    def enable_widget(self, type_: str, name: str):
        widget = self.get_widget(type_, name)
        widget.Enable(True)

    @reiterate_func_with_two_args
    def disable_widget(self, type_: str, name: str):
        widget = self.get_widget(type_, name)
        widget.Enable(False)

    def bind_widget(self, type_: str, name: str, func, event: wx.Event):
        widget = self.get_widget(type_, name)
        self.Bind(event, func, widget)

    @reiterate_func_with_one_arg
    def create_btn(self, name: str, *, auto_name_label=False, label=NOT_NAMED, pos=wx.DefaultPosition, width=-1, height=-1, style=0):
        if auto_name_label and label != self.NOT_NAMED:
            raise Exception
        self.create_widget('btn', name, label=name if auto_name_label else label, pos=pos,
                           size=(width, height), style=style)

    @reiterate_func_with_one_arg
    def create_static_text(self, name: str, *, auto_name_label=False, colon=False, label=NOT_NAMED, pos=wx.DefaultPosition, width=-1, height=-1, style=0):
        if auto_name_label and label != self.NOT_NAMED:
            raise Exception
        if colon:
            label_ = (name if auto_name_label else label) + ':'
        else:
            label_ = name if auto_name_label else label
        self.create_widget('static_text', name, label=label_, pos=pos, size=(width, height), style=style)

    @reiterate_func_with_one_arg
    def create_text_ctrl(self, name: str, *, value=wx.EmptyString, pos=wx.DefaultPosition, width=-1, height=-1, style=0):
        self.create_widget('text_ctrl', name, value=value, pos=pos, size=(width, height), style=style)

    @reiterate_func_with_two_args
    def create_combobox(self, name: str, choices: list[str], *, value=wx.EmptyString, pos=wx.DefaultPosition, width=-1, style=0):
        self.create_widget('combobox', name, value=choices[0] if choices and value == wx.EmptyString else value, pos=pos, size=(width, -1),
                           choices=choices, style=style)

    @reiterate_func_with_two_args
    def bind_btn(self, name: str, func):
        self.bind_widget('btn', name, func, event=wx.EVT_BUTTON)

    @reiterate_get_func_with_one_arg
    def get_btn(self, name: str) -> wx.Button | tuple[wx.Button]:
        return self.get_widget('btn', name)

    @reiterate_get_func_with_one_arg
    def get_static_text(self, name: str) -> wx.StaticText | tuple[wx.StaticText]:
        return self.get_widget('static_text', name)

    @reiterate_get_func_with_one_arg
    def get_text_ctrl(self, name: str) -> wx.TextCtrl | tuple[wx.TextCtrl]:
        return self.get_widget('text_ctrl', name)

    @reiterate_get_func_with_one_arg
    def get_combobox(self, name: str) -> wx.ComboBox | tuple[wx.ComboBox]:
        return self.get_widget('combobox', name)


if __name__ == '__main__':
    ...
